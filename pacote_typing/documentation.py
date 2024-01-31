"""
Typing é um módulo utilizado para fornecer anotações de tipo(type hints) para objetos python.

Principais módulos e funções:

    obj: type - Indica que obj é instância de type, ou é do tipo type

    obj: Callable[[typearg, typearg], typereturn ] - Indica que obj é uma função com argumentos de typearg, e retorno de tipo typereturn
    
    obj: Waitable[return_type] - Indica que o objeto é do tipo Waitable, e pode esperar sua resolução ou rejeição com await obj
    
    obj: Coroutine[return_type, arg_type, exception_type] - Indica que o objeto é uma função asyncrona[corrotina]

    obj: Type[Class] -  Indica que o obj deve ser uma subclass de Class, ou a própria class, ou seja Type[type] indica que o objeto deve ser uma classe não uma instância
    
    obj: Optional[str] - Indica que objeto pode ser do tipo Str ou None
    
    obj: Literal["Yes", "No"]- Indica que o objeto só pode receber esses dois valores, é util para restringir valores
    
    obj: Union[str, int] - Indica que obj pode ser do tipo str ou int, ou ambos
    
    obj: Dict[int, str] - Indica que o objeto é um dicionário, de chaves do tipo int, e valores str
    
    obj: List[int] - Indica que objeto é uma lista de inteiros
    
    obj: Tuple[int, str, dict] - Indica que o objeto é uma tupla com três argumentos de tipos[int, str, dict]
    
    obj: Sequence[int] - Indica que o obj deve ser uma Sequence ORDENADA de inteiros, Sequence é todo objeto que é um iterable, e é indexavel
    
    obj: Iterable[Union[str, int]] - Indica que obj pode ser um iterable[ou iterator], que contenha tipos str, ou int, ou seja apenas indica que o objeto tem que ser percorrivel por for, e não precisa ter indice
    
    
    obj: Collection[int] - Indica que objeto deve ser do tipo Collection, ou seja o objeto tem que ter comprimento(__len__), tem que ser um iterable(__iter__), e tem que suportar `in` operator(__contains__) 
    
    
    obj: Any - Indica que obj pode ser qualquer tipo
    
    obj: Iterator - Indica que objeto tem que ser um iterator(__iterable__, __next__), ou seja tem que ser percorrivel por For, e tem que ser possivel usar next para mostrar o proximo valor
    
    obj: OrderedDict - Indica que objeto tem que ser um dicionário ordenado
    
    
    
    NewType(name, class) - Cria um novo tipo baseado em uma classe existente
    
    Type(name) - Retorna uma classe de nome passado
    
    Type[name] - Indica que objeto deve ser uma child class de name, ou deve ser a classe name
    
    T = TypeVar("T") - TypeVar é um recurso utilizado que a variavel é de qualquer tipo ou de um tipo desconhecido, é util para indicar que uma função aceita qualquer tipo, ou para não definir o tipo da função logo de cara, isso permite maior generalidade
    
    
    TypeVar
    
    TYPE_CHECKING - variavel retorna true se não for o módulo em execução(__main__)

Tipar extruturas:
    não varia: 
        def foo(name:str, ...) -> str - Define a tipagem de argumentos e retorno da função

    Modo Correto:
        typing.Dict[str, int] | typing.Dict[type_key, type_value] - Tipa um dicionário

        typing.List[str] 

    Modo direto(não recomendado por não ser tão compativel com mypy):


        dict[str, int] | dict[type_key: type_value] - Tipa um dicionario

        list[int] - Tipa uma lista 
    
"""
import typing

lista: typing.List = [
    1,
    1,
    1,
    1,
    1,
]


Pessoa = typing.Dict[str, typing.Union[str, typing.List[typing.Union[int, str]]]]

p1: Pessoa = {
    "name": "Carl",
    "surname": "John",
    "age": 30,
    "sex": "M",
    "marital_status": "Married",
    "children": [1, 2, 3, 4, 5],
}
