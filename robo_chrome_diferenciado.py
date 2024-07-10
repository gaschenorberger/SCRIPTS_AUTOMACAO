from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Selenium\ChromeTestProfile"

def iniciar_navegador(com_debugging_remoto=True):
    chrome_driver_path = ChromeDriverManager().install()
    service = Service(executable_path=chrome_driver_path)
    
    chrome_options = Options()
    if com_debugging_remoto:
        remote_debugging_port = 9222
        chrome_options.add_experimental_option("debuggerAddress", f"localhost:{remote_debugging_port}")
    
    navegador = webdriver.Chrome(service=service, options=chrome_options)
    return navegador

navegador = iniciar_navegador(com_debugging_remoto=True)
navegador.quit()


