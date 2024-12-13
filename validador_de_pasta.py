#FUNÇÃO: Percorre uma pasta para ver se tem arquivos faltando de uma lista especifica

'''Por ex: Foi feito um robô para baixar arquivos, nesse robô ele percorre uma lista de numeros para baixar esses arquivos, mas no final
voce quer conferir se todos os arquivos foram baixados corretamente na pasta'''


import os
import pandas as pd

caminho_pasta = r"C:\Users\gabriel.alvise\Desktop\DOWNLOAD'S XML" #Pasta que quer verificar se esta faltando arquivos

caminho_planilha = r"C:\Users\gabriel.alvise\Desktop\ROBOS\conferir_xml.xlsx" #Planilha com a lista de arquivos

df = pd.read_excel(caminho_planilha)
numeros_esperados = df['Numeros'].astype(str).tolist() #Nome da coluna

arquivos_esperados = [f"{numero}.xml" for numero in numeros_esperados]

arquivos_na_pasta = os.listdir(caminho_pasta)

arquivos_faltando = [arquivo for arquivo in arquivos_esperados if arquivo not in arquivos_na_pasta]

if arquivos_faltando:
    df_faltando = pd.DataFrame({'Arquivos Faltando': arquivos_faltando})
    caminho_saida = r"C:\Users\gabriel.alvise\Desktop\ROBOS\result.xlsx" #Planilha com resultados dos arquivos que estão faltando
    df_faltando.to_excel(caminho_saida, index=False)

    print("Arquivos faltando:")
    for arquivo in arquivos_faltando:
        print(arquivo)
    print(f"\nLista de arquivos faltantes salva em: {caminho_saida}")
else:
    print("Todos os arquivos estão presentes.")
