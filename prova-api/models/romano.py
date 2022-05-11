
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
                num+=roman[s[i]]
                i+=1
        return num
    def intToRoman(self, num):
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
        x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
        thousands = m[num // 1000]
        hundreds = c[(num % 1000) // 100]
        tens = x[(num % 100) // 10]
        ones = i[num % 10]
  
        ans = (thousands + hundreds +
           tens + ones)
  
        return ans


class Config:
    host = "jdbc:mysql://localhost:3306/provadatabase"
    user = "root"
    password = "1234"
    db = "provadatabase"


class romano(BaseModel):
        
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
        classe = romano()
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
        classe = romano()
        resultado_final = classe.quebrar_string(array)
        resultado_final = classe.traduzir_romano_array(resultado_final)
        classe.quickSort(resultado_final, 0, len(resultado_final)-1)
        return resultado_final
    

    