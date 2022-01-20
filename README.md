<h1 align="center">Criando FTP Em Python</h1>

Muitas pessoas e empresas usam o FTP para transferência de arquivos, mas acabam não gostando das opções de frameworks do mercado. Com isso, a biblioteca `pyftpdlib` veio para ajudar as pessoas criarem os seus próprios sistemas e com mais desempenho.

## Links:
* [PyPi](http://pyftpdlib.readthedocs.io/)
* [Documentação](http://pyftpdlib.readthedocs.io/)
* [Permissões](https://pyftpdlib.readthedocs.io/en/latest/api.html#pyftpdlib.authorizers.DummyAuthorizer)


## Instalando a biblioteca
```bash
pip install pyftpdlib
```

***

## Importando
```python
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
```

***

## Criando o gerenciador de conexões
```python
authorizer = DummyAuthorizer()
authorizer.add_user("masso", "senha123", r"D:\Masso13\Arquivos\Python\Github\Criando-FTP-Em-Python", "elradrmw")
```

***

## Criando o manipulador
```python
handler = FTPHandler
handler.authorizer = authorizer
```

***

## Criando o server
```python
with FTPServer(("192.168.2.11", 21), handler) as server:
    server.max_cons = 5
    server.max_cons_per_ip = 2
    server.serve_forever()
```