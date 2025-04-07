from dataclasses import dataclass
from datetime import datetime
import re
@dataclass
class PerfilSchema:
    def validatinName(self):
        while True:
            name = input("Insira seu nome: ")
            namepattern = r'^[a-zA-Z]+$'
            if re.match(namepattern,name):
                return name.upper()
            else:
                print("Vai se fuder otário coloca um nome namoral vey")
    def validatinAge(self):
        current_year: int = datetime.now().year
        while True:
            try:
                age = int(input("Insira seu ano de nascimento: "))
                if len(str(age)) == 4 and (current_year - age) >= 16 and age > 1925:
                    validAge = current_year - age
                    return validAge
                elif age < 1925:
                    print("Tabom espertinho, então voce tem mais de 100 anos é???")
                else:
                    print("é preciso ter no mínimo 16 anos para cadastrar-se!")
            except:
                print("Favor inserir um valor de ano válido")
    def validatinPhone(self):
        while True:
            try:
                ddd_phone = int(input("Insira seu DDD: "))
                if len(str(ddd_phone)) == 2:
                    break
                else:
                    print("Favor inserir um numero valido de DDD(2 digitos inteiros)")
            except:
                print("Favor inserir um numero valido de DDD(2 digitos inteiros)")
        while True:
            try:
                phone_number = int(input("Insira seu numero de telefone: "))
                if len(str(phone_number)) == 9:
                    return f"({ddd_phone}){phone_number}"
                else:
                    print("Insira um digito válido de telefone(9 digitos inteiros)")
            except:
                print("Insira um digito válido de telefone(9 digitos inteiros)")
    def validatinCountry(self):
        while True:
            country = input("Insira o seu país: ")
            namepattern = r'^[a-zA-Z]+$'
            if re.match(namepattern,country):
                return country.upper()
            else:
                print("Vai se fuder otário coloca um nome namoral vey")
    def get_datas(self):
        self.dataPerfil = (self.validatinName(),self.validatinAge(),self.validatinPhone(),self.validatinCountry())
    def printData(self):
        print(self.dataPerfil)
