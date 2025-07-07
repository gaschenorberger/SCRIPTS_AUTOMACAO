# Marcar inicio da execução do robô

def marcarInicio():
    inicioExe = datetime.now()
    print(f"Robô iniciado em: {inicioExe.strftime('%d/%m/%Y %H:%M:%S')}")
