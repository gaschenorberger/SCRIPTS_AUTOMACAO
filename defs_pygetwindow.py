import pygetwindow as gw

def consultar_janelas_abertas(): #PRINTA O NOME DE TODAS AS JANELAS E ABAS ABERTAS
    janelas = gw.getAllTitles()
    print(janelas)

consultar_janelas_abertas()

def ativar_pagina(nome_pag): #ATIVA A PAGINA
    window = gw.getWindowsWithTitle(nome_pag)[0]
    window.activate()

ativar_pagina('GitHub - Google Chrome')



# EXEMPLO PARA LOOP, ENQUANTO NAO TIVER UMA JANELA ABERTA ELE ESPERA ATE ESTAR ABERTA PARA CONTINUAR

while not any('Kaspersky VPN' in janela for janela in consultar_janelas_abertas()):
        print("Esperando o Kaspersky VPN abrir...")
        time.sleep(1) 

print("Kaspersky VPN foi aberto!")
