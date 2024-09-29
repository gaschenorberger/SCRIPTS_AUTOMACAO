#TEM COMO FUNÇÃO BUSCAR UMA PALAVRA NA TELA E CLICAR EM CIMA DELA

#pip install pyautogui pytesseract pillow
#https://github.com/UB-Mannheim/tesseract/wiki -- instalar tesseract
#https://github.com/tesseract-ocr/tessdata/blob/main/por.traineddata -- idioma português

import pyautogui
import pytesseract
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  
def buscar_e_clicar(palavra):
    screenshot = ImageGrab.grab()
    
    texto_tela = pytesseract.image_to_data(screenshot, lang='por', output_type=pytesseract.Output.DICT)
    
    for i, palavra_tela in enumerate(texto_tela['text']):
        if palavra.lower() == palavra_tela.lower():
            x = texto_tela['left'][i]
            y = texto_tela['top'][i]
            
            pyautogui.moveTo(x + 10, y + 10) 
            pyautogui.click()
            print(f'Palavra "{palavra}" encontrada e clicada nas coordenadas ({x}, {y})!')
            return
    
    print(f'Palavra "{palavra}" não encontrada na tela.')

buscar_e_clicar('')


