from validInputs import validInputs
from colorama import Fore, Style

inputs_obj = validInputs()

runningApp = True

def structureApp():
    global runningApp
    print(Fore.MAGENTA+ "")
    print("MENU")
    print("Insira: 1 - logar | 2 - Cadastrar | 3 - Sair")
    try:
        choice = int(input("Insira a opção desejada: " + Style.RESET_ALL))
        if choice == 1:
            inputs_obj.login()
        elif choice == 2:
            inputs_obj.registry()
        elif choice == 3:
            runningApp = False
        else:
            print("")
            print(Fore.RED + "alguma das opções do menu...")
    except:
        print("")
        print(Fore.RED + "Insira uma das opções do MENU!")
def runApp():
    print("")
    print(Fore.YELLOW + "BEM VINDO AO APP")
    while runningApp:
        structureApp()
    print("")
    print(Fore.YELLOW + "APLICAÇÃO FINALIZADA..." + Style.RESET_ALL)
    print("")