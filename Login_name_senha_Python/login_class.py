import sqlite3
from colorama import Fore, Style

class UserDataClass:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def login(self):
        conn = sqlite3.connect('credentials.db')
        cursor = conn.cursor()


        auth_user_data = (self.username,self.password)
        cursor.execute('''
            SELECT 1 FROM credentials WHERE username = ? AND password = ?;
        ''',auth_user_data)

        authCheck = cursor.fetchone()

        if authCheck:
            print(Fore.GREEN +'''
                AUTHENTICAÇÃO REALIZADA COM SUCESSO!
            '''+ Style.RESET_ALL)
        else:
            print(Fore.RED +'''
                AUTHENTICAÇÃO FALHA!
                Username ou Senha Invalidos!
            '''+ Style.RESET_ALL)
