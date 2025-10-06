"""
O objetivo dessa função é tirar um print da tela completa de um site, sem precisar utilizar scroll
"""

def tirarPrints(driver, path):
    """ DOCUMENTAÇÃO DESSA FUNÇÃO


    Captura um screenshot de **toda a página** (full page screenshot),
    independente do tamanho da tela/viewport visível no momento.

    Essa função utiliza o Chrome DevTools Protocol (CDP), que permite
    acessar comandos internos do ChromeDriver. 
    O comando "Page.captureScreenshot" faz o navegador gerar um print 
    da página inteira, incluindo áreas que não estão visíveis sem scroll.

    Parâmetros
    ----------
    driver : selenium.webdriver.Chrome
        Instância do navegador controlada pelo Selenium.
    path : str
        Caminho (com nome do arquivo) onde o screenshot será salvo.
        Exemplo: "tabela.png"

    Funcionamento
    -------------
    1. Executa o comando interno do Chrome "Page.captureScreenshot".
    2. O resultado vem em Base64 (string binária).
    3. Decodifica o Base64 para bytes de imagem.
    4. Salva os bytes em formato PNG no caminho especificado.

    Observação
    ----------
    - Funciona somente no Chrome/Chromium, pois depende do CDP.
    - Garante captura da página inteira, diferente do método padrão 
    `driver.save_screenshot`, que captura apenas a parte visível.
    """

    # Envia comando ao Chrome DevTools para capturar a tela completa
    result = driver.execute_cdp_cmd(
        "Page.captureScreenshot",
        {"format": "png", "captureBeyondViewport": True}
    )

    # Decodifica o resultado em Base64 para bytes
    with open(path, "wb") as f:
        f.write(base64.b64decode(result['data']))
        
