def reconhecer_cod_captcha():
    screenshot = pyautogui.screenshot(region=(564, 520, 150, 50)) #MUDAR AS COORDENADAS DE ACORDO COM O COMPUTADOR
    screenshot.save("screenshot.png")

    image_path = "screenshot.png"
    img = Image.open(image_path)
    gray_img = img.convert("L")

    enhanced_img = ImageOps.autocontrast(gray_img)

    binarized_img = enhanced_img.point(lambda x: 0 if x < 128 else 255, '1')

    processed_image_path = "printprocessado.png"
    binarized_img.save(processed_image_path)

    recognized_text = pytesseract.image_to_string(binarized_img, lang='por')
    recognized_text_cleaned = recognized_text.replace(" ", "").replace("\t", "").replace("\n", "").strip()
    recognized_text_cleaned = recognized_text_cleaned.upper()

    processed_image_path, recognized_text_cleaned
    print("Texto reconhecido:", recognized_text_cleaned)
