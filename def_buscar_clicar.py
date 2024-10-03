#TEM COMO FUNÇÃO BUSCAR UMA PALAVRA/FRASE NA TELA E CLICAR EM CIMA DELA

#pip install pyautogui pytesseract pillow opencv-python numpy
#https://github.com/UB-Mannheim/tesseract/wiki -- instalar tesseract
#https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata -- idioma português -- COLOCAR NA PASTA DO TESSERACT (C:\Program Files\Tesseract-OCR\tessdata)

from PIL import ImageGrab
from PIL import Image
import pyautogui
import pytesseract
import cv2
import numpy as np
import difflib

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 

def buscar_e_clicar(texto_busca, ocorrencia=1, horizontal=10, vertical=10, click=1, coordenadas=None, max_tentativas=50):

    def preprocessar_imagem(imagem):
        imagem_cinza = cv2.cvtColor(np.array(imagem), cv2.COLOR_BGR2GRAY)
        _, imagem_binaria = cv2.threshold(imagem_cinza, 150, 255, cv2.THRESH_BINARY)
        return Image.fromarray(imagem_binaria)
    
    def tentar_deteccao(imagem, config):
        try:
            return pytesseract.image_to_data(imagem, lang='por', output_type=pytesseract.Output.DICT, config=config)
        except Exception as e:
            print(f"Erro na detecção: {e}")
            return None
        
    def normalizar_texto(texto):
        return ''.join(c for c in texto if c.isalnum()).lower()
    
    def palavras_similares(palavra_detectada, palavra_busca):
        similaridade = difflib.SequenceMatcher(None, normalizar_texto(palavra_detectada), normalizar_texto(palavra_busca)).ratio()
        return similaridade > 0.8 

    tentativa = 0
    encontrado = False

    if coordenadas:
        x, y = coordenadas
        bbox = (x - 50, y - 50, x + 50, y + 50)
    else:
        bbox = None 

    while tentativa < max_tentativas and not encontrado:
        print(f"Tentativa {tentativa + 1} de {max_tentativas} para encontrar '{texto_busca}'")

        screenshot = ImageGrab.grab(bbox=bbox)  
        if coordenadas:
            print(f'Capturando área: {coordenadas}')
        else:
            print('Capturando tela inteira.')

        largura_imagem, altura_imagem = screenshot.size  

        imagem_processada = preprocessar_imagem(screenshot)
        config = '--oem 3 --psm 6'
        texto_tela = tentar_deteccao(imagem_processada, config)

        if not texto_tela:
            print(f'Não foi possível detectar o texto.')
            tentativa += 1
            continue
        
        palavras_detectadas = texto_tela['text']
        coordenadas_detectadas = list(zip(texto_tela['left'], texto_tela['top'], texto_tela['width'], texto_tela['height']))

         # Verifica as coordenadas de cada palavra
        print("Palavras e suas coordenadas detectadas:")
        for i, palavra in enumerate(palavras_detectadas):
            if palavra.strip() != "":
                print(f"Palavra: '{palavra}', Coordenadas: ({texto_tela['left'][i]}, {texto_tela['top'][i]})")

        ocorrencias_encontradas = [
            (x, y, largura, altura)
            for i, palavra in enumerate(palavras_detectadas)
            if palavras_similares(palavra, texto_busca.split()[0])
            for x, y, largura, altura in [coordenadas_detectadas[i]]
        ]

        if len(ocorrencias_encontradas) >= ocorrencia:
            x, y, largura, altura = ocorrencias_encontradas[ocorrencia - 1]
            encontrado = True
        else:
            print(f'A ocorrência {ocorrencia} da palavra "{texto_busca}" não foi encontrada.')
            tentativa += 1

    if encontrado:
        if 0 <= x <= largura_imagem and 0 <= y <= altura_imagem:
            pyautogui.moveTo(x + horizontal, y + vertical)
            if click == 2:
                pyautogui.doubleClick()
            else:
                pyautogui.click()
            print(f'Clique na ocorrência {ocorrencia} da palavra "{texto_busca}" nas coordenadas ({x + horizontal}, {y + vertical})!')
        else:
            print(f'Coordenadas ({x}, {y}) estão fora dos limites da tela.')
    else:
        print(f'Não foi possível encontrar a palavra "{texto_busca}" após {max_tentativas} tentativas.')
        
buscar_e_clicar('palavra/frase', click=1 (1 click) ou click=2 (doubleClick), horizontal=50 (opcional), vertical=50 (opcional), ocorrencia=2 (caso haja duas palavras iguais)) #CUSTOMIZE DA FORMA NECESSÁRIA
buscar_e_clicar('x', click=2, horizontal=50, vertical=50, ocorrencia=2) #EXEMPLO 


