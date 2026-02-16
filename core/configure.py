import winreg
import json
import pyodbc
import pandas as pd

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)

def list_sql_instances():
    instances = set()

    # Checa tanto o hive 64-bit quanto o 32-bit
    registry_paths = [
        r"SOFTWARE\Microsoft\Microsoft SQL Server\Instance Names\SQL",
        r"SOFTWARE\WOW6432Node\Microsoft\Microsoft SQL Server\Instance Names\SQL",
    ]

    for path in registry_paths:
        try:
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path) as key:
                i = 0
                while True:
                    try:
                        # name = nome da instância (MSSQLSERVER, SQLEXPRESS, etc.)
                        # value = identificador interno (ex.: MSSQL16.MSSQLSERVER) — não vamos usar
                        name, value, _ = winreg.EnumValue(key, i)
                        instances.add(name)
                        i += 1
                    except OSError:
                        # WinError 259 -> acabou
                        break
        except FileNotFoundError:
            # Esse caminho pode não existir em algumas instalações — segue o baile
            pass

    # Normaliza saída: instância padrão MSSQLSERVER sem barra
    normalized = []
    for name in sorted(instances, key=lambda s: (s.upper() != "MSSQLSERVER", s.upper())):
            normalized.append(f"\\{name}")
    
    return normalized

def list_dbs():
        #======== CONFIG HERE ========
    SERVER   = ".{}".format(data["SQL_INSTANCE"])   # Ex: 'localhost\\SQLEXPRESS' ou '10.0.0.5'
    DATABASE = "master"# << DB
    DRIVER   = '{ODBC Driver 17 for SQL Server}'  # or '{ODBC Driver 18 for SQL Server}'
    # =================================
    conn_str = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'



    conn = pyodbc.connect(conn_str)

    # Executa sp_spaceused
    query = "SELECT name FROM sys.databases;"

    df = pd.read_sql(query, conn)
    dbs = []
    for names in df["name"]:
        dbs.append(names)
    
    return dbs

def configure():
    
    insts = list_sql_instances()
    
    while True:
        print("Escolha a instância do banco que será utilizada:")
        c = 0
        for i in insts:
            print('{} - {}'.format(c, i))
            c += 1
        try:
            x = int(input(""))

            selected_instance = insts[int(x)]
            
            data["SQL_INSTANCE"] = selected_instance
            
            with open("config.json", "w") as f:
                json.dump(data, f)

            break
        except:
            print("O valor selecionado não é válido.")
        
    dbs = list_dbs()

    while True:
        print("Escolha a instância do banco que será utilizada:")
        c = 0
        for db in dbs:
            print('{} - {}'.format(c, db))
            c += 1
        try:
            x = int(input(""))

            selected_DB = dbs[int(x)]
            
            data["SELECTED_DB"] = selected_DB
            with open("config.json", "w") as f:
                json.dump(data, f)
            print("**WatchTower Configurado com sucesso!**")
            break
        except:
            print("O Valor selecionado é inválido!")

    


