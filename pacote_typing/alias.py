"""
Um type alias é uma forma de criar um novo nome para um tipo existente. como uma string, um número, uma lista, uma função, etc. Exemplo: 

    Nome = str # cria um alias de tipo para str - Nome indica que é uma instância de str
    meu_nome: Nome = "Copilot" - Indica que meu_nome é do tipo nome
    
Type Alias é recurso muito util para dar mais contexto a um objeto de tipo complexo, ou objeto com tipagem longo, então nomeando o tipo dessa objeto com type alias isso pode gerar mais contexto na hora de inferir o tipo do objeto


"""
from typing import Sequence

ConnectionOptions = dict[str, str]
Address = tuple[str, int]
Server = tuple[Address, ConnectionOptions]


def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...
