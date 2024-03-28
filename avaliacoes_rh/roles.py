from rolepermissions.roles import AbstractUserRole

class Rh(AbstractUserRole):
    available_permissions = {
        'cadastrar_usuarios': True,
        'realizar_avaliacao': True,
    }


class Avaliador(AbstractUserRole):
    available_permissions = {
        'realizar_avaliacao': True,
    }

    