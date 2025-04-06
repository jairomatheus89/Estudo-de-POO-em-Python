from colorama import Fore, Style

class PerfilUsuario:
    def __init__(self,nome,email,idade,telefone,pais):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.telefone = telefone
        self.pais = pais

    def exibir_dados(self):
        uppername = str(self.nome).upper()
        print(Fore.GREEN + f'''
            ALL USER DATA*
            Name: {uppername}
            Email: {self.email}
            Age: {self.idade} years
            Phone: {self.telefone}
            Country: {self.pais}
        ''' + Style.RESET_ALL)