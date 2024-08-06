import pyautogui

max_tentativas = 1
tentativas = 0
while tentativas < max_tentativas:
    try:
        tentativas += 1
        bx = pyautogui.locateCenterOnScreen('bx.png', confidence=0.8)
        pyautogui.doubleClick(bx)
        print('Abrindo BX')
        continue
    except:
        print('Não encontrei o BX')
        break
