from dataclasses import dataclass
import re
from colorama import Fore, Style

@dataclass
class ValidationOfInputs:
    
    def validName(self):        
        while True:
            lettersOnlyPattern = r'^[a-zA-Z]+$'
            name = input("Digite seu nome de usuário: ")
            if re.match(lettersOnlyPattern,name) and len(name) > 4:
                nameupper = name.upper()
                return nameupper
            else:
                print(Fore.RED + '''
                    Nome invalido
                    Deve possuir mais de 4 caracters
                    Não pode haver caracteres especiais, apenas letras
                ''' + Style.RESET_ALL)

    def checkvalidEmail(self):
        emailRegexPattern = r'.*@.*'
        while True:
            email = input("Digite um e-mail valido: ")
            if re.match(emailRegexPattern,email) and len(email) > 8:
                return email
            else:
                print(Fore.RED + "Insira a estrutura de um email valido por favor!" + Style.RESET_ALL)

    def checkAge(self):
        while True:
            try:
                age = int(input("Insira sua idade: "))
                if age >= 16:
                    return age
                else:
                    print(Fore.RED + "É preciso ter no mínimo 16 anos para se cadastrar" + Style.RESET_ALL)
            except:
                print(Fore.RED + "Digite uma idade válida" + Style.RESET_ALL)

    def checkPhone(self):
        while True:
            try:
                phoneDDD = int(input("Insira o DDD do seu telefone: "))
                if len(str(phoneDDD)) == 2:
                    break
                else:
                    print(Fore.RED + "insira um numero DDD valido com dois digitos" + Style.RESET_ALL)
            except:
                print(Fore.RED + "Insira um numero DDD de dois digitos" + Style.RESET_ALL)
        while True:
            try:
                phoneNumber = int(input("Insira um numero de telefone válido de 9 digitos: "))
                if len(str(phoneNumber)) == 9:
                    return f"({phoneDDD}){phoneNumber}"
            except:
                print(Fore.RED + "insira um numero de 9 digitos inteiros válidos" + Style.RESET_ALL)
        
    def checkCountry(self):
        while True:
            lettersOnlyPattern = r'^[a-zA-Z]+$'
            country = input("Digite o nome do seu país: ")
            if re.match(lettersOnlyPattern,country) and len(country) > 4:
                countryupper = country.upper()
                return countryupper
            else:
                print(Fore.RED + '''
                    Nome invalido
                    Deve possuir mais de 4 caracters
                    Não pode haver caracteres especiais, apenas letras
                ''' + Style.RESET_ALL)

