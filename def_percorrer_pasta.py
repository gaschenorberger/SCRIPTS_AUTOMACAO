#PERCORRE A PASTA DESEJADA E TRAZ O CAMINHO DE CADA ARQUIVO PRESENTE E SALVA EM UMA PLANILHA EXCEL

import os
import time
import openpyxl #pip install openpyxl
import openpyxl.workbook

planilha_caminhos = openpyxl.load_workbook("spedFiscal\\caminhos.xlsx") #ARQUIVO XLSX 
pagiCaminhos= planilha_caminhos['caminhos_icms'] #PAGINA DA PLANILHA

def percorrer_arq_pasta():
    caminho_pasta = 'C:\\Users\\gabriel.alvise\\Desktop\\TESTES\\AUTO-PY\\spedFiscal\\ICMS'
    os.startfile(caminho_pasta) #ABRE A PASTA

    time.sleep(1)
    caminhos_dos_arquivos = [] #ARMAZENA TODOS OS CAMINHOS

    for raiz, _, arquivos in os.walk(caminho_pasta): #PERCORRE OS ARQUIVOS E TRAZ O CAMINHO
        for arquivo in arquivos:
            caminho_completo = os.path.join(raiz, arquivo)
            caminhos_dos_arquivos.append(caminho_completo)

    for index, caminho in enumerate(caminhos_dos_arquivos, start=1): #SALVA OS CAMINHOS NA PLANILHA
        print(caminho)
        pagiCaminhos.cell(row=index, column=1).value = caminho

    planilha_caminhos.save("pasta_salvamento\\arquivo_excel.xlsx") #SALVA A PLANILHA 
    print('Todos os arquivos salvos!')
