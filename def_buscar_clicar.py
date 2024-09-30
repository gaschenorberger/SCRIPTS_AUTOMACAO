#TEM COMO FUNÇÃO BUSCAR UMA PALAVRA/FRASE NA TELA E CLICAR EM CIMA DELA

#pip install pyautogui pytesseract pillow opencv-python numpy
#https://github.com/UB-Mannheim/tesseract/wiki -- instalar tesseract
#https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata -- idioma português

from PIL import ImageGrab
import pyautogui
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 

def preprocessar_imagem(imagem):
    imagem_cinza = cv2.cvtColor(np.array(imagem), cv2.COLOR_BGR2GRAY)
    
    _, imagem_binaria = cv2.threshold(imagem_cinza, 150, 255, cv2.THRESH_BINARY)
    
    return Image.fromarray(imagem_binaria)

def buscar_e_clicar(texto_busca, horizontal=10, vertical=10, click=1):
    screenshot = ImageGrab.grab()
    largura_imagem, altura_imagem = screenshot.size  
    
    imagem_processada = preprocessar_imagem(screenshot)
    
    config = '--oem 3 --psm 6'  
    
    texto_tela = pytesseract.image_to_data(imagem_processada, lang='por', output_type=pytesseract.Output.DICT, config=config)
    
    palavras_detectadas = texto_tela['text']
    coordenadas_detectadas = list(zip(texto_tela['left'], texto_tela['top']))

    #Verifica as coordenadas de cada palavra    
    """print("Palavras e suas coordenadas detectadas:")
    for i, palavra in enumerate(palavras_detectadas):
        if palavra.strip() != "":
            print(f"Palavra: '{palavra}', Coordenadas: ({texto_tela['left'][i]}, {texto_tela['top'][i]})")"""
    
    if texto_busca.lower() in ' '.join(palavras_detectadas).lower():
        palavras_busca = texto_busca.split()
        for i in range(len(palavras_detectadas) - len(palavras_busca) + 1):
            frase_atual = ' '.join(palavras_detectadas[i:i+len(palavras_busca)])
            
            if frase_atual.lower() == texto_busca.lower():
                x, y = coordenadas_detectadas[i]
                
                if 0 <= x <= largura_imagem and 0 <= y <= altura_imagem:
                    pyautogui.moveTo(x + horizontal, y + vertical)
                    if click == 2:
                        pyautogui.doubleClick()
                        print(f'Double click na frase/palavra "{texto_busca}" nas coordenadas ({x + horizontal}, {y + vertical})!')
                    else:  
                        pyautogui.click()
                        print(f'Clique na frase/palavra "{texto_busca}" nas coordenadas ({x + horizontal}, {y + vertical})!')
                else:
                    print(f'Coordenadas ({x}, {y}) estão fora dos limites da tela.')
                return
    
    print(f'Frase/palavra "{texto_busca}" não encontrada na tela.')

buscar_e_clicar('palavra/frase', click=1 (1 click) ou click=2 (doubleClick), horizontal=50 (opcional), vertical=50 (opcional)) #CUSTOMIZE DA FORMA NECESSÁRIA
buscar_e_clicar('x', click=2, horizontal=50, vertical=50) #EXEMPLO 


