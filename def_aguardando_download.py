def aguardando_download(pasta_download_origem, nome_arquivo):
    pasta_download_origem = r"C:\Users\gabriel.alvise\Downloads"
    nome_arquivo = 'arquivo_completo.zip'

    while any([filename.endswith('.crdownload') or filename.endswith('.part') 
               for filename in os.listdir(pasta_download_origem)]):
        print("Aguardando o download ser concluído...")
        time.sleep(2)  

    while not os.path.exists(os.path.join(pasta_download_origem, nome_arquivo)):
        print(f"Verificando se {nome_arquivo} foi baixado...")
        time.sleep(2)

    print(f"Download concluído: {nome_arquivo} está na pasta.")

aguardando_download(pasta_download_origem, nome_arquivo)
