from datetime import datetime

# Marcar inicio da execução do robô

def marcarInicio():
    inicioExe = datetime.now()
    print(f"Robô iniciado em: {inicioExe.strftime('%d/%m/%Y %H:%M:%S')}")



# OBTER DIA ATUAL (31/07/2024)
dataAtual = datetime.now()
dataAtual = dataAtual.strftime('%d/%m/%Y')
print(dataAtual)

