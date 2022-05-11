# prova-fast-api
 
# REST API utilizando o framewok de fast-api

Esta é uma API básica que apresenta uma solução para o problema proposto na prova técnica da empresa Studio Sol

A aplicação está dividia em três partes: o main.py(onde tem a parte responsável pela implementação dos métodos e a parte do REST), o romano.py(onde contém toda a lógica utilizada para execução do programa) e um pasta dedidacado a um banco de dados que foi inutilizado(eu ja tinha um banco feito no MySQL e deixei ele disponível caso precisasse)


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
    content-length: 26 
    content-type: application/json 
    date: Wed,11 May 2022 01:11:01 GMT 
    server: uvicorn 

    {
       "number": "LX",
       "value": 60
    }



# Romano.py e a lógica utilizada para resolver o problema
### Começando pela:  

    class Solution()
### Que contém os métodos:

     def romanToInt(s)
     def intToRoman(num)
     
São dois métodos focados na tradução dos numerais para que possam ser utilizados no código quando necessário, o primeiro método utiliza um dicionário e um loop básico para decifrar um númeral escrito em romano e transformar em um int que é retornado ao final da execução, já o intToRoman é uma engenharia reversa do primeiro método mas utilizando listas e divisões para quebrar o número e transformá-lo em uma string romana, no contexto do código o romanToInt() foi utilizado para pegar o resultado da quebra da string proposta e transformar em um int para a retirada do maior resultado no final do código, o intToRoman foi utilizado no final do código para poder retornar o símbolo romano do maior numeral presente na string.

### Seguindo para a próxima classe:  

    class romano(Base Model)
### Que contém os métodos:

     def quebra_string(self, sentence)
     def partition(self, arr, low, high)
     def quickSort(self, arr, low, high)
     def traduzir_romano_array(self, array)
     def execute_final(self, array)

