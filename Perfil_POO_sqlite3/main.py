from sqlite_bridge import get_post_sqlite
from colorama import Fore, Style, Back
from time import sleep

print(Fore.WHITE + "#"*60)
print("--- Bem-Vindo ao RioPretoBook cadastre seu perfil ---".center(60))
while True:
    print(Fore.WHITE + "#"*60 + Style.RESET_ALL)
    print(Fore.WHITE + "Menu".center(60) + Style.RESET_ALL)
    print(Fore.WHITE + "1 - cadastrar perfil | 2 - Sair".center(60) + Style.RESET_ALL)
    try:
        choice = int(input(Fore.WHITE + "Inserir opção:\n".center(60) + Style.RESET_ALL))
        if choice == 1:
            get_post_sqlite()
        elif choice == 2:
            print(Fore.YELLOW + "Finalizando aplicação...")
            sleep(1)
            print("FINISHED!" + Style.RESET_ALL)
            break
        else:
            print("")
            print("Insira uma das opções exibidas no MENU!".center(60).upper())
            print("")
    except:
        print("")
        print("Insira apenas um numero inteiro dentre as opções disponiveis".upper())
        print("")