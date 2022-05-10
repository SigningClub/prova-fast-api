import re
from tkinter import E
from typing import List, Optional
from fastapi import Request
from pydantic import BaseModel, Field

from db.conexaoBD import *

import re
class Solution(object):
   def romanToInt(self, s):
      """
      :type s: str
      :rtype: int
      """
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=roman[s[i]]
            i+=1
      return num


class Config:
    host = "bd_rt_teste.mysql.dbaas.com.br"
    user = "bd_rt_teste"
    password = "j1cr.9WCS72021"
    db = "bd_rt_teste"


class Usuario(BaseModel):

    id_email_usuario: str = Field(None, alias="USR_id_email_usuario")
    codigo_tipo_usuario: int = Field(None, alias="TPU_cod_tipo_usuario")
    nome_usuario: str = Field(None, alias="USR_nome_usuario")
    senha_usuario: str = Field(None, alias="USR_nome_usuario")

    def set_usuario(self, id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario):
        self.id_email_usuario = id_email_usuario
        self.codigo_tipo_usuario = codigo_tipo_usuario
        self.nome_usuario = nome_usuario
        self.senha_usuario = senha_usuario

    def inserir(self, id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario):
        self.set_usuario(id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario)
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"INSERT INTO TB_USR_Usuarios_RT (USR_id_email_usuario, TPU_cod_tipo_usuario, USR_nome_usuario, USR_senha_usuario) "
        sql += f"VALUES ('{id_email_usuario}', {codigo_tipo_usuario}, '{nome_usuario}', '{senha_usuario}')"
        bd.executa_DML(sql)

    def alterar(self, id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario):
        self.set_usuario(id_email_usuario, codigo_tipo_usuario, nome_usuario, senha_usuario)
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"UPDATE TB_USR_Usuarios_RT "
        sql += f"SET TPU_cod_tipo_usuario = '{codigo_tipo_usuario}' "
        sql += f", USR_nome_usuario = '{nome_usuario}' "
        sql += f", USR_senha_usuario = '{senha_usuario}' "
        sql += f"WHERE USR_id_email_usuario = '{id_email_usuario}'"
        bd.executa_DML(sql)

    def excluir(self, id_email_usuario):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"DELETE FROM TB_USR_Usuarios_RT "
        sql += f"WHERE USR_id_email_usuario = '{id_email_usuario}'"
        bd.executa_DML(sql)

    def consulta(self):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_USR_Usuarios_RT"
        resultado = bd.executa_DQL(sql)
        return resultado

    def consulta_usuario(self, id_email_usuario):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_USR_Usuarios_RT WHERE USR_id_email_usuario = '{id_email_usuario}'"
        resultado = bd.executa_DQL(sql)
        return resultado

    def verifica_login(self, id_email_usuario, senha_usuario):
        bd = ConexaoBD(Config.host, Config.user, Config.password, Config.db)
        sql = f"SELECT * FROM TB_USR_Usuarios_RT WHERE USR_id_email_usuario = '{id_email_usuario}' AND USR_senha_usuario = '{senha_usuario}'"
        resultado = bd.executa_DQL(sql)
        try:
            extracao = resultado[0]
            print(extracao[0])

            if id_email_usuario in extracao[0] :
                print("EMAIL ENCONTRADO!")
            if senha_usuario in extracao[2]:
                print("Senha correta!")
                return True
        except:
            return False
        
    def quebrar_string(self, sentence):
        romano = ["I", "V", "X", "L" , "C" , "D" , "M"]
        resultado_final = []
        for i in range(len(sentence)):
            try:
                if(sentence[i] not in romano):
                    resultado = sentence.split(sentence[i])
                    sentence = resultado[1]
            except:
                resultado_final = resultado
                pass
        return resultado_final
    
    def partition(self, arr, low, high):
        i = (low - 1)
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
 
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)
    
    def quickSort(self, arr, low, high):
        classe = Usuario()
        if len(arr) == 1:
            return arr
        if low < high:
            pi = classe.partition(arr, low, high)
            classe.quickSort(arr, low, pi-1)
            classe.quickSort(arr, pi+1, high)
    
    def traduzir_romano_array(self, array):
        ob1 = Solution()
        retorno = []
        for i in range(len(array)):
            retorno.append(ob1.romanToInt(array[i]))
        return retorno
    def execute_final(self, array):
        classe = Usuario()
        resultado_final = classe.quebrar_string(array)
        resultado_final = classe.traduzir_romano_array(resultado_final)
        classe.quickSort(resultado_final, 0, len(resultado_final)-1)
        return resultado_final
    def intToRoman(self, num):
  
    # Storing roman values of digits from 0-9
    # when placed at different places
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
    # Converting to roman
        thousands = m[num // 1000]
        hundreds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]
  
        ans = (thousands + hundreds +
           tens + ones)
  
        return ans

    

class login:
    def __init__(self, request:Request):
        self.request: Request = request
        self.erros: List = []
        self.username: Optional[str]= None
        self.password: Optional[str]= None
    async def load_data(self):
        form = await self.request.form()
        self.username = form.get('USR_id_email_usuario')
        self.password = form.get('USR_senha_usuario')
    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.erros.append("Email is not valid")
        if not self.password or not len(self.password)>=4:
            self.erros.append("Senha is not valid")
        if not self.erros:
            return True
        return False