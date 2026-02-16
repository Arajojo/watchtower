from core.configure import *
from checks.cpu import *
from checks.memory import *
from checks.disk import *
from checks.db import *

def menu():
    print(r"""
 ==========================================         
+------------------------------------------+          
|            __    __   ______             |
|           |  |/\|  | |_    _|            |
|           |        |   |  |              |
|            \__/\__/    |__|              |
|                   .n.                    |  
|        /___\          _.---.  \ _ /      |
|        [|||]         (_._ ) )--;_) =-    |
|        [___]           '---'.__,' \      |
|        }-=-{                    |        |
|        |-" |                             |
|        |.-"|                p            |
| ~^=~^~-|_.-|~^-~^~ ~^~ -^~^~|\ ~^-~^~-   |
| ^   .=.| _.|__  ^       ~  /| \          |
|  ~ /:. \" _|_/\    ~      /_|__\  ^      |
| .-/::.  |   |""|-._    ^   ~~~~          |
|   `===-'-----'""`  '-.              ~    |
|                  __.-'      ^            |
+------------------------------------------+          
 =========BEM VINDO AO WATCHTOWER!=========
          """)
    while True:

        try:

            print("===================MENU===================\n\n1 - Check Up Geral\n2 - Limpeza dos dados temporários\n3 - Gerar relatório da Saúde da maquina\n4 - Configurar WatchTower\n0 - Sair.\n\n==========================================")
            x = int(input(""))
            match x:
                case 1:
                    results = []

                    results.append(check_cpu())
                    results.append(check_memory())
                    results.append(check_disk())
                    results.append(check_db())
                    for r in results:
                        print(r)
                    print("Pressione Enter para voltar ao Menu.")
                    input("")
                case 2:
                    pass
                    print("Pressione Enter para voltar ao Menu.")
                    input("")
                case 3:
                    pass
                    print("Pressione Enter para voltar ao Menu.")
                    input("")
                case 4:
                    configure()
                    print("Pressione Enter para voltar ao Menu.")
                    input("")
                case 0:
                    print("Já que quer sair, não volte mais!")
                    break
                case _:
                    print("**O VALOR SELECIONADO É INVÁLIDO!**")
                    print("Pressione Enter para Continuar..")
                    input("")
        except Exception as err:
            print("Ocorreu um erro ao selecionar alguma opção: {}".format(err))
            print("Pressione Enter para retorar ao menu..")
            input("")