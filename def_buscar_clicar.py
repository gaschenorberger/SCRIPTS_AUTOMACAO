#TEM COMO FUNÇÃO BUSCAR UMA PALAVRA/FRASE NA TELA E CLICAR EM CIMA DELA

#pip install pyautogui pytesseract pillow opencv-python numpy
#https://github.com/UB-Mannheim/tesseract/wiki -- instalar tesseract
#https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata -- idioma português -- COLOCAR NA PASTA DO TESSERACT (C:\Program Files\Tesseract-OCR\tessdata)

from PIL import ImageGrab
import pyautogui
import pytesseract
import cv2
import numpy as np
import difflib

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 

def preprocessar_imagem(imagem):
    imagem_cinza = cv2.cvtColor(np.array(imagem), cv2.COLOR_BGR2GRAY)
    
    _, imagem_binaria = cv2.threshold(imagem_cinza, 150, 255, cv2.THRESH_BINARY)
    
    return Image.fromarray(imagem_binaria)

def palavras_similares(palavra_detectada, palavra_busca):
    similaridade = difflib.SequenceMatcher(None, palavra_detectada, palavra_busca).ratio()
    return similaridade > 0.8 

def buscar_e_clicar(texto_busca, ocorrencia=1, horizontal=10, vertical=10, click=1, coordenadas=None):
    if coordenadas:
        x, y, largura, altura = coordenadas
        screenshot = ImageGrab.grab(bbox=(x, y, x + largura, y + altura)) 
    else:
        screenshot = ImageGrab.grab()  

    largura_imagem, altura_imagem = screenshot.size  

    imagem_processada = preprocessar_imagem(screenshot)
    
    config = '--oem 3 --psm 6' 
    
    texto_tela = pytesseract.image_to_data(imagem_processada, lang='por', output_type=pytesseract.Output.DICT, config=config)
    
    palavras_detectadas = texto_tela['text']
    coordenadas_detectadas = list(zip(texto_tela['left'], texto_tela['top']))

    # Verifica as coordenadas de cada palavra
    """print("Palavras e suas coordenadas detectadas:")
    for i, palavra in enumerate(palavras_detectadas):
        if palavra.strip() != "":
            print(f"Palavra: '{palavra}', Coordenadas: ({texto_tela['left'][i]}, {texto_tela['top'][i]})")"""
    
    ocorrencias_encontradas = []
    palavras_busca = texto_busca.split()

    for i in range(len(palavras_detectadas)):
        if palavras_similares(palavras_detectadas[i], palavras_busca[0]):
            frase_atual = palavras_detectadas[i:i + len(palavras_busca)]
            if len(frase_atual) == len(palavras_busca) and all(palavras_similares(frase_atual[j], palavras_busca[j]) for j in range(len(palavras_busca))):
                x, y = coordenadas_detectadas[i]
                ocorrencias_encontradas.append((x, y))

    if len(ocorrencias_encontradas) >= ocorrencia:
        x, y = ocorrencias_encontradas[ocorrencia - 1]  
    else:
        print(f'A ocorrência {ocorrencia} da palavra "{texto_busca}" não foi encontrada na tela.')
        return

    if coordenadas:
        x, y, _, _ = coordenadas

    if 0 <= x <= largura_imagem and 0 <= y <= altura_imagem:
        pyautogui.moveTo(x + horizontal, y + vertical)

        if click == 2:
            pyautogui.doubleClick()
            print(f'Double click na ocorrência {ocorrencia} da palavra "{texto_busca}" nas coordenadas ({x + horizontal}, {y + vertical})!')
        else: 
            pyautogui.click()
            print(f'Clique na ocorrência {ocorrencia} da palavra "{texto_busca}" nas coordenadas ({x + horizontal}, {y + vertical})!')
    else:
        print(f'Coordenadas ({x}, {y}) estão fora dos limites da tela.')

buscar_e_clicar('palavra/frase', click=1 (1 click) ou click=2 (doubleClick), horizontal=50 (opcional), vertical=50 (opcional), ocorrencia=2 (caso haja duas palavras iguals), coordenadas=(x, y)) #CUSTOMIZE DA FORMA NECESSÁRIA
buscar_e_clicar('x', click=2, horizontal=50, vertical=50, ocorrencia=2, coordenadas=(x, y)) #EXEMPLO 


