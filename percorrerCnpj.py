import openpyxl
import openpyxl.workbook

planilha_caminhos = openpyxl.load_workbook(r"robo_bx\BasesNovas.xlsx")
pagiCaminhos = planilha_caminhos['Planilha1']

def extracaoCnpj(alinha): #VAI PERCORRER CADA LINHA
    cnpjs = []
    for row in pagiCaminhos.iter_rows(min_row=alinha):  
        nome_empresa = row[0].value  #PRIMEIRA COLUNA (A)
        cnpj = row[1].value  #SEGUNDA COLUNA (B)
        if cnpj:
            cnpjs.append((nome_empresa, cnpj))  

    return cnpjs

#EXEMPLO DE COMO CHAMAR EM OUTRA FUNÇÃO

def exemplo(linha):
    alinha = linha
    cnpjs = extracaoCnpj(alinha)  

    for nome_empresa, cnpj in cnpjs:

exemplo(1)
