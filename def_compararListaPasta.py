# Comparar uma lista txt x pasta. Verificar quais arquivos estão faltando na pasta que estão na lista

def compararPastaLista():

    caminhoNotas = r"C:\Users\gabriel.alvise\Desktop\VSCODE-ROBOS\telaRobos\scripts\NOTAS.txt" # CAMINHO DO ARQUIVO TXT A SER COMPARADO
    with open(caminhoNotas, 'r') as file:
        chaves = [linha.strip() for linha in file.readlines()]

    caminho = r"C:\Users\gabriel.alvise\Desktop\DOWNLOAD'S ROBOS\XML" # CAMINHO COM TODOS OS ARQUIVOS JA BAIXADOS A SEREM COMPARADOS

    arquivos = [
        os.path.splitext(nome)[0].replace('NFE-', '') # Aqui como fiz para verificar xml, tive que retirar NFE do nome do arquivo, para melhor comparação
        for nome in os.listdir(caminho)
        if nome.lower().endswith('.xml') # Utilizando endswith para pegar apenas xml da pasta
    ]

    chaveBaixada = []
    chaveNaoBaixada = []

    for chave in chaves:
        encontrado = any(chave in arquivo for arquivo in arquivos) 

        if encontrado:
            chaveBaixada.append(chave)
        else:
            chaveNaoBaixada.append(chave)



    totalNaoBaixada = len(chaveNaoBaixada) #Total de chaves que nao estao presentes na pasta
    totalArquivos = len(arquivos) #Total arquivos da pasta
    totalLista = len(chaves) #Total Chaves da lista

    print(totalLista, "chaves na lista")
    print(totalArquivos, "arquivos na pasta")
    print(totalNaoBaixada, "chaves não baixadas")


    print("CHAVES NAO ENCONTRADAS NA PASTA: ", ', '.join(chaveNaoBaixada)) # Retorna em texto todas as chaves nao presentes
