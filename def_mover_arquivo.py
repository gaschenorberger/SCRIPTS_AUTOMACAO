def mover_arquivo(pasta_origem, pasta_destino, nome_do_arquivo):
    caminho_origem = os.path.join(pasta_origem, nome_do_arquivo)
    caminho_destino = os.path.join(pasta_destino, nome_do_arquivo)

    if os.path.exists(caminho_origem):
        shutil.move(caminho_origem, caminho_destino)
        print(f"Arquivo movido para: {caminho_destino}")
    else:
        print(f"Arquivo {nome_do_arquivo} não encontrado na pasta de origem.")
        
#Exemplo
pasta_download_origem = r"C:\Users\gabriel.alvise\Downloads"
pasta_matriz_saidas = r"C:\Users\gabriel.alvise\Desktop\ROBOS\robo_download_nfe\matriz\saidas"
nome_do_arquivo = 'MATRIZ - 123456 - 2024_10_23.zip'  #Nome do arquivo

mover_arquivo(pasta_download_origem, pasta_matriz_saidas, nome_do_arquivo)
