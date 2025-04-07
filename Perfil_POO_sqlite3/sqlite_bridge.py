import sqlite3
from perfilClass import PerfilSchema

def get_post_sqlite():
    user_data = PerfilSchema()
    user_data.get_datas()

    # INIT SQLITE CONNECTION
    conn = sqlite3.connect('perfil.db')
    cursor = conn.cursor()

    username_exists_check = cursor.execute("SELECT EXISTS (SELECT 1 FROM perfis WHERE username=(?));",(user_data.dataPerfil[0],))
    checkname_result = bool(username_exists_check.fetchone()[0])

    phone_exists_check = cursor.execute("SELECT EXISTS (SELECT 1 FROM perfis WHERE phone=(?));",(user_data.dataPerfil[2],))
    checkphone_result = bool(phone_exists_check.fetchone()[0])

    if not checkname_result and not checkphone_result:
        cursor.execute('''
            INSERT OR IGNORE INTO perfis (username,age,phone,country) VALUES (?,?,?,?);
        ''', user_data.dataPerfil)
        conn.commit()
        conn.close()
        print("Perfil de usuário cadastrado com sucesso!")
    else:
        print('''
            TENTATIVA DE CADASTRO FALHOU!
            USERNAME ou TELEFONE JA CADASTRADOS!
        ''')
        conn.close()