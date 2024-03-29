"""
Conjunto de metódos para fazer operações com filedescriptors(arquivos em aberto, processos em execução)

os.Readonly
os.RDWR


file descriptor operators: 
    os.open(way, O_Permission, mode:511) -> filedescriptor:int - Abre um processo com determinadas permissões no SO
    
    os.close(fd) - Encerra um processo em execução

    os.device_encoding(fd) - Retorna o encoding de um filedescriptor

    fchmod(fd, mode(maskoctal)) - Altera as permissões de um file descriptor

    os.fchown(fd, uid, gid) - Altera os proprietarios de um processo/file descriptor

    os.close(fd) - Encerra um processo em execução

    os.fstat - Retorna o status/perfil de um file descriptor

    

"""
import os
os.open()

