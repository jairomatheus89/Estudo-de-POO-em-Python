from colorama import Fore, Style
import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        self.valor = 0.00
    def converting_saldo_brl(self,valorConvert):
        self.valorConvert = locale.currency(valorConvert,grouping=True)
    def exibir_saldo(self):
        self.converting_saldo_brl(self.saldo)
        print(Fore.BLUE + f"Saldo atual do(a) {self.titular} é: " + Fore.GREEN + f"{self.valorConvert}" + Style.RESET_ALL)
    def deposito(self,valor):
        self.saldo += valor
        self.converting_saldo_brl(valor)
        print(Fore.BLUE + f"Você recebeu um deposito de: " + Fore.GREEN + f"{self.valorConvert}" + Style.RESET_ALL)
    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.converting_saldo_brl(valor)
            print(Fore.BLUE + f"Você fez um saque de: " + Fore.GREEN + f"{self.valorConvert}" + Style.RESET_ALL)
        else:
            self.converting_saldo_brl(valor)
            print(Fore.RED + f"Voce não possui {self.valorConvert} para realizar o saque, por favor consulte seu Saldo!")
conta_da_marina = ContaBancaria("Marina",200.69)
conta_do_jairo = ContaBancaria("Jairo", 666.89)
print(Fore.YELLOW + f"Conta de {conta_da_marina.titular}" + Style.RESET_ALL)
conta_da_marina.exibir_saldo()
conta_da_marina.deposito(50)
conta_da_marina.sacar(30)
conta_da_marina.exibir_saldo()
print("")
print(Fore.YELLOW + f"Conta de {conta_do_jairo.titular}" + Style.RESET_ALL)
conta_do_jairo.exibir_saldo()
conta_do_jairo.sacar(667)
conta_do_jairo.exibir_saldo()



