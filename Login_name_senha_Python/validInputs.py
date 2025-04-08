from login_class import UserDataClass
from sqlite_schema import CredentialsClassSql
from colorama import Fore, Style
from getpass import getpass

class validInputs:
    def login(self):
        print(Fore.BLUE + "")
        print("Login:")
        username = input("Insira um nome de usuário: ")
        password = getpass("Insira sua senha: ")
        login_obj = UserDataClass(username.lower(),password)
        login_obj.login()
    def registry(self):
        print(Fore.BLUE + "")
        print("Cadastro: ")
        username = input("Insira um nome de usuário: ")
        password = getpass("Insira sua senha: ")
        reg_obj = CredentialsClassSql(username.lower(),password)
        reg_obj.reg_db_query()