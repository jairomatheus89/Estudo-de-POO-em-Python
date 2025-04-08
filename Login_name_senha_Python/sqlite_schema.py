import sqlite3
from colorama import Fore, Style

class CredentialsClassSql:
    def __init__(self,username,password):  
        self.username = username
        self.password = password
        pass

    def reg_db_query(self):
        conn = sqlite3.connect('credentials.db')
        cursor = conn.cursor()
        table_name = "credentials"

        try:
            cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {table_name}(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT CHECK(length(username) <= 40) UNIQUE,
                    password TEXT NOT NULL
                );
            ''')
        except:
            print("Já tem uma tabela")

        try:
            cursor.execute('''
                INSERT INTO credentials (username,password) VALUES (?,?)
            ''',(self.username,self.password))
            print(Fore.GREEN +'''
                Cadastrado com sucesso papai!
            ''' + Style.RESET_ALL)
        except:
            print(Fore.RED +'''
                esse username ja existe papaizito!
            '''+ Style.RESET_ALL)
        finally:
            conn.commit()
            conn.close()