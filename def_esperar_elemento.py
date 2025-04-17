def esperar_elemento(navegador, xpath, tempo=10):
    """
    Espera até que um elemento esteja presente na página, usando o XPath fornecido.

    :param navegador: Instância do navegador Selenium.
    :param xpath: XPath do elemento a ser aguardado.
    :param tempo: Tempo máximo de espera em segundos (padrão: 10).
    :return: Lista de elementos encontrados ou None se não encontrar.
    """
    try:
        elementos = WebDriverWait(navegador, tempo).until(
            EC.presence_of_all_elements_located((By.XPATH, xpath))
        )
        return elementos
    except Exception as e:
        print(f"[!] Erro ao esperar pelo elemento: {e}")
        return None
