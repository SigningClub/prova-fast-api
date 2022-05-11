# prova-fast-api
 
# REST API utilizando o framewok de fast-api

Esta é uma API básica que apresenta uma solução para o problema proposto na prova técnica da empresa Studio Sol

A aplicação está dividia em três partes: o main.py(onde tem a parte responsável pela implementação dos métodos e a parte do REST), o romano.py(onde contém toda a lógica utilizada


## Instalar

    pip install -r requirements.txt

## Iniciar aplicativo
No diretório do main.py executar o comando:

    uvicorn main:app --reload


# REST API

Os métodos presentes na REST API

## Método search

### Request

`POST /search`

    curl -X 'POST' \'http://127.0.0.1:8000/romano?string_input=AXXBLX' \-H 'accept: application/json' \ -d ''

### Response

    HTTP/1.1 200 OK
    Date: Thu, 24 Feb 2011 12:36:30 GMT
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2

    []

## Create a new Thing

### Request

`POST /thing/`

    curl -i -H 'Accept: application/json' -d 'name=Foo&status=new' http://localhost:7000/thing

### Response

    HTTP/1.1 200 OK
    content-length: 26 
    content-type: application/json 
    date: Wed,11 May 2022 01:11:01 GMT 
    server: uvicorn 

    {
       "number": "LX",
       "value": 60
    }

