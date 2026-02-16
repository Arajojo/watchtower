import pyodbc
import pandas as pd
import json

import warnings
warnings.filterwarnings(
    "ignore",
    message=".*pandas only supports SQLAlchemy connectable.*",
    category=UserWarning
)





def check_db():
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    #======== CONFIG HERE ========
    SERVER   = ".{}".format(data["SQL_INSTANCE"])   # Ex: 'localhost\\SQLEXPRESS' ou '10.0.0.5'
    DATABASE = data["SELECTED_DB"] # << DB
    DRIVER   = '{ODBC Driver 17 for SQL Server}'  # or '{ODBC Driver 18 for SQL Server}'
    # =================================


    conn_str = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'



    conn = pyodbc.connect(conn_str)

    # Executa sp_spaceused
    query = "EXEC sp_spaceused;"

    df = pd.read_sql(query, conn)
    usage = df['database_size'].to_string(index=False)
    name = df['database_name'].to_string(index=False)

    conn.close()

    return {
        "type": "Database",
        "name": name,
        "usage": usage
    }

