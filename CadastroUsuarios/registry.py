from PerfilUsuarioClass import PerfilUsuario
from validInputs import ValidationOfInputs
from dataclasses import dataclass

@dataclass
class RegistryUser:

    def registry(self):
        validInputs = ValidationOfInputs()

        name = validInputs.validName()
        user_email = validInputs.checkvalidEmail()
        age = validInputs.checkAge()
        phone = validInputs.checkPhone()
        country = validInputs.checkCountry()

        objPerfil = PerfilUsuario(name,user_email,age,phone,country)
        objPerfil.exibir_dados()

        