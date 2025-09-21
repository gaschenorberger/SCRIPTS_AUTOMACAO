import json
import http
import time

# API CNPJ
    def get_cnpj_data(cnpj):
        conn = http.client.HTTPSConnection("receitaws.com.br")
        headers = { 'Accept': "application/json" }
        
        while True:
            try:
                conn.request("GET", f"/v1/cnpj/{cnpj}", headers=headers)
                res = conn.getresponse()
                data = res.read()
                json_data = json.loads(data.decode("utf-8"))
                
                # Se status == OK, deu certo, então retorna
                if json_data.get("status") == "OK":
                    print("API OK")
                    return json_data
                else:
                    print(f"[AVISO] Consulta falhou ou atingiu limite. Tentando de novo em 20 segundos... Resposta: {json_data}")
                    time.sleep(20)

            except Exception as e:
                print(f"[ERRO] Falha ao consultar CNPJ: {e}. Tentando de novo em 20 segundos...")
                time.sleep(20)


# EXEMPLO DE USO

get_cnpj_data("xxxxxxxxxxxxxx") # SEM A FORMATAÇÃO DO CNPJ
