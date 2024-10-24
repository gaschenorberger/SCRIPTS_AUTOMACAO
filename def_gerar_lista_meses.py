import calendar
from datetime import datetime

def gerar_lista_meses(ano_inicio, ano_fim, mes_inicio=1):
    lista_meses = []
    for ano in range(ano_inicio, ano_fim + 1):
        for mes in range(mes_inicio, 13):
            inicio_mes = f"01/{mes:02d}/{ano}"
            ultimo_dia_mes = calendar.monthrange(ano, mes)[1]
            fim_mes = f"{ultimo_dia_mes:02d}/{mes:02d}/{ano}"
            lista_meses.append((inicio_mes, fim_mes))
        mes_inicio = 1 
    return lista_meses

lista_meses = gerar_lista_meses(2018, 2024, 8)
    for inicio, fim in lista_meses:
        print(f"'{inicio}', '{fim}'") #01/01/2018 -- 31/01/2018

        data_inicio = f'{inicio}'
        data_final = f'{fim}'

        data_ini = navegador.find_element(By.XPATH, '//*[@id="form1:dtIniInputDate"]') 
        data_fim = navegador.find_element(By.XPATH, '//*[@id="form1:dtFinInputDate"]') 
        navegador.execute_script("arguments[0].value = arguments[1]", data_ini, f'{data_inicio}')
        navegador.execute_script("arguments[0].value = arguments[1]", data_fim, f'{data_final}')
