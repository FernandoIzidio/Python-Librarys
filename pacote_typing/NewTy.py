"""
NewType é um recurso utilizado em situação onde se deseja criar um novo tipo baseado em um tipo existente, para fornecer mais segurança e precisão. Exemplo:

IDUsuario = NewType("IdUsuario", int) - IdUsuario é uma childclass de int, oque implica em dizer que o tipo IDUsuario pode ser usado normalmente para representar tipos da parent class, mas tipos int(números quaisquer) não pode reprentar tipos IdUsuario.

Ou seja IDusuario pode ser usado como inteiro qualquer, mas um inteiro qualquer não pode representar uma instância de IdUsuario
"""
from typing import NewType


IdUsuario = NewType("IdUsuario", int)  # Classe id usuário


numero1 = IdUsuario(45)
print(
    numero1,
    isinstance(numero1, int),
)
