from PIL import Image, ImageEnhance
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = r'C:\Users\gabriel.alvise\Pictures\Screenshots\Captura de tela 2025-01-29 110225.png'
image = Image.open(image_path)

image = image.convert('L') 
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(2) 

width, height = image.size
upper_half = image.crop((0, 0, width, height // 2))
lower_half = image.crop((0, height // 2, width, height))

extracted_text_upper = pytesseract.image_to_string(upper_half, lang='por')
extracted_text_lower = pytesseract.image_to_string(lower_half, lang='por')

extracted_text = extracted_text_upper + '\n' + extracted_text_lower

print("Texto extraído:\n")
print(extracted_text)

with open('conexoes_extraidas.txt', 'w', encoding='utf-8') as file:
    file.write(extracted_text)

