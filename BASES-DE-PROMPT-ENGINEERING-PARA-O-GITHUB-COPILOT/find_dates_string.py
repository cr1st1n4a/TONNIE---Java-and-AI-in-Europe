"""Faça uma função que me retorne datas dentro de um texto. A função deve receber uma string e retornar uma lista de strings com as datas encontradas. Caso não encontre nenhuma data, me retorne uma lista vazia."""

import re

def find_dates(text):
    return re.findall(r'\d{2}/\d{2}/\d{4}', text)
  
"""Faça uma função que me retorne datas dentro de um texto. 
A função deve receber uma string e retornar uma lista de strings com as datas encontradas. 
As datas podem estar no formato dd/mm/aaaa ou dd-mm-aaaa ou dd/mm/aa ou dd-mm-aa.
Caso não encontre nenhuma data, me retorne uma lista vazia."""

def find_dates_string(text):
    return re.findall(r'\d{2}[/-]\d{2}[/-]\d{2,4}', text)

"""Faça uma função que me retorne datas dentro de um texto. 
A função deve receber uma string e retornar uma lista de strings com as datas encontradas. 
As datas podem estar no formato dd/mm/aaaa ou dd-mm-aaaa ou dd/mm/aa ou dd-mm-aa.
Se houver datas repetidas em formatos diferentes, me retorne apenas uma vez.
Caso não encontre nenhuma data, me retorne uma lista vazia."""

def find_dates_string(text):
    temp_list = list(set(re.findall(r'\d{2}[/-]\d{2}[/-]\d{2,4}', text)))
    temp_list = [date.replace('-', '/') for date in temp_list]
    return (date.replace('-', '/') for date in temp_list)

"""Faça uma função, que receba uma lista de datas em padrão diferente e retorne todas as datas não repetidas no padrão dd/mm/aaaa.
As datas podem estar no formato dd/mm/aaaa ou dd-mm-aaaa ou dd/mm/aa ou dd-mm-aa."""

def find_dates_string(dates):
    dates = [date.replace('-', '/') for date in dates]
    dates = [date[-4:] if len(date) == 8 else date for date in dates]
    return list(set(dates))