def mover_arquivo(pasta_origem, pasta_destino, nome_do_arquivo):
    """
    Move um arquivo da pasta de origem para a pasta de destino.

    :param pasta_origem: Caminho da pasta de onde o arquivo será movido.
    :param pasta_destino: Caminho da pasta para onde o arquivo será movido.
    :param nome_do_arquivo: Nome do arquivo a ser movido.
    """
    # Caminhos completos para o arquivo de origem e destino
    caminho_origem = os.path.join(pasta_origem, nome_do_arquivo)
    caminho_destino = os.path.join(pasta_destino, nome_do_arquivo)

    # Verifica se o arquivo existe na pasta de origem
    if os.path.exists(caminho_origem):
        # Move o arquivo para a pasta de destino
        shutil.move(caminho_origem, caminho_destino)
        print(f"Arquivo movido para: {caminho_destino}")
    else:
        print(f"Arquivo {nome_do_arquivo} não encontrado na pasta de origem.")

#Exemplo
pasta_download_origem = r"C:\Users\gabriel.alvise\Downloads"
pasta_matriz_saidas = r"C:\Users\gabriel.alvise\Desktop\ROBOS\robo_download_nfe\matriz\saidas"
nome_do_arquivo = 'MATRIZ - 123456 - 2024_10_23.zip'  #Nome do arquivo

mover_arquivo(pasta_download_origem, pasta_matriz_saidas, nome_do_arquivo)
