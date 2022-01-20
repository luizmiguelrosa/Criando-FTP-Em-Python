## Importando
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

## Criando o gerenciador de conexões
authorizer = DummyAuthorizer()
authorizer.add_user("masso", "senha123", r"D:\Masso13\Arquivos\Python\Github\Criando-FTP-Em-Python", "elradrmw")

## Criando o manipulador
handler = FTPHandler
handler.authorizer = authorizer

## Criando o server
with FTPServer(("192.168.2.11", 21), handler) as server:
    server.max_cons = 5
    server.max_cons_per_ip = 2
    server.serve_forever()