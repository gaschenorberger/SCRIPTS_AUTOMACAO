import os
impor time

def renomear_arquivo(pasta_downloads, nome_do_arquivo):
    novo_nome_base = os.path.join(pasta_downloads, nome_do_arquivo)
    extensao = '.zip'
    
    while os.path.exists(novo_nome_base + extensao):
        novo_nome_base = os.path.join(pasta_downloads, f"{nome_do_arquivo}")
        
    arquivo_baixado = os.path.join(pasta_downloads, "arquivo_completo.zip")  
    if os.path.exists(arquivo_baixado):
        os.rename(arquivo_baixado, novo_nome_base + extensao)
        print(f"Arquivo renomeado para: {novo_nome_base + extensao}")
    else:
        print("Arquivo para renomear não encontrado.")

pasta_download_origem = r"C:\Users\gabriel.alvise\Downloads"
nome_arq = f'MATRIZ - {notas_fiscais} - {inicio}'
nome_do_arquivo = nome_arq.replace('/', '_')
print(nome_do_arquivo)

if os.path.exists(os.path.join(pasta_download_origem, "arquivo_completo.zip")):
    renomear_arquivo(pasta_matriz_saidas, nome_do_arquivo)
    break  
else:
    print("Download falhou. Tentando novamente...")
    time.sleep(2)  
