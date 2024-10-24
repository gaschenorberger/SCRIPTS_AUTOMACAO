def verificar_download_temporario(pasta_downloads):
        arquivos = os.listdir(pasta_downloads)
        
        if any(arquivo.endswith('.crdownload') for arquivo in arquivos):
            print("Download em andamento (arquivo temporário encontrado).")
            return True
        else:
            print("Nenhum download em andamento.")
            return False
          
#EXEMPLO

pasta_download_origem = r'C:\Users\gabriel.alvise\Downloads'
verificar_download_temporario(pasta_download_origem)

#Verifica se na pasta downloads tem um arquivo web que está sendo baixado 
