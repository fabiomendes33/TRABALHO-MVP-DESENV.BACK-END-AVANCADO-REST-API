# Minha API em REST

Este pequeno projeto faz parte do material diático da Disciplina **Desenvolvimento Full Stack Avançado** 

O objetivo aqui é apresetar uma API emplementada seguindo o estilo REST.

As principais tecnologias que serão utilizadas aqui é o:
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [OpenAPI3](https://swagger.io/specification/)
 - [SQLite](https://www.sqlite.org/index.html)
 - [LOCUST](:https://docs.locust.io/en/stable/)

---
### Instalação da documentaçao para a API REST SWAGGER


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---
### Executando o servidor


Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

---
### Acesso no browser

Abra o [http://localhost:5000/#/](
    
) no navegador para verificar o status da API em execução.

---
### Instalação da documentaçao para a execuçao do Docker


Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:
1 – Atualizar o Sistema
O primeiro passo é atualizar a lista de pacotes do Ubuntu. Para isso entre com o seguinte comando:; ,

$ sudo apt update

2 - Instalar pré-requisitos
Instale pacotes de pré-requisitos para permitir ao APT o uso de pacotes seguros HTTPS.

$ sudo apt install apt-transport-https ca-certificates curl software-properties-common


3 – Adicionar chave GPG
Vamos adicionar a chave para garantir a validade dos pacotes vindos do repositório do Docker.

$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

4 – Adicionar repositório Docker ao Ubuntu
Vamos adicionar o repositório Docker as fontes de pacotes do Ubuntu.

$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

5 – Atualizar a lista de pacotes
Atualize novamente a lista dos pacotes.

$ sudo apt update

6 – Instalar o Docker
Vamos instalar o Docker no Ubuntu.

$ sudo apt install docker-ce

7 – Verificar a instalação
Para garantir que tudo deu certo vamos verificar se o Docker está em execução.

$ sudo systemctl status docker
$ docker --version

8 - Por padrão o comando Docker só pode ser executado pelo usuário usando SUDO. Para facilitar o uso, vamos adicionar nosso usuário do sistema ao grupo docker, assim não precisamos usar SUDO e digitar senha as nossa execuções do comando.

$ sudo usermod -aG docker ${USER}
$ su - ${USER}

$  sudo docker build -t rest-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$  sudo docker run -p 5000:5000 rest-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.



### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ sudo docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ sudo docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ sudo docker container ls --all
>```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>```
>$  sudo docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ sudo docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).

INSTALAÇÃO PARA A EXECUÇAO DO LOCUST

$ pip3 install locust

Valide sua instalação

$ locust -V
locust 2.16.1 from /usr/local/lib/python3.10/site-packages/locust (python 3.10.6)

Executar a ENV ativada

$ source env/bin/activate


Executar Locust

$ locust -f test/load_test/load_test.py

Depois Abrir outro terminal para deixar executando seguinte comando.


$ flask run --host 0.0.0.0 --port 5000

Depois que entrar no Programa Locust voce vai definir a URl e depois fazer testes de CARGA.

http://localhost:5000/