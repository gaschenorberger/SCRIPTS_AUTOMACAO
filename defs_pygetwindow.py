import pygetwindow as gw

def consultar_janelas_abertas(): #PRINTA O NOME DE TODAS AS JANELAS E ABAS ABERTAS
    janelas = gw.getAllTitles()
    print(janelas)

consultar_janelas_abertas()

def ativar_pagina(nome_pag): #ATIVA A PAGINA
    window = gw.getWindowsWithTitle(nome_pag)[0]
    window.activate()

ativar_pagina('GitHub - Google Chrome')
