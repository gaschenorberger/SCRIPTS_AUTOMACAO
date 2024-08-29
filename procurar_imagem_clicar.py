import pyautogui

max_tentativas = 1
tentativas = 0
while tentativas < max_tentativas:
    try:
        tentativas += 1
        x = pyautogui.locateCenterOnScreen('(imagem).png', confidence=0.8)
        pyautogui.doubleClick(x)
        print('Abrindo (x)')
        continue
    except:
        print('Não encontrei o BX')
        break


"""2 OPÇÃO"""


import pyautogui
import time
import random
import mousekey

mkey = mousekey.MouseKey()

def procurar_imagem(nome_arquivo, confidence=0.8, region=None, max_tentativas=60, horizontal=0, vertical=0, acao='clicar'):
    """
    Procura uma imagem na tela e executa uma ação (clicar ou mover o mouse).
    
    :param nome_arquivo: O caminho para o arquivo de imagem a ser procurado.
    :param confidence: A confiança mínima para encontrar a imagem.
    :param region: A região da tela onde procurar a imagem. Deve ser uma tupla (x, y, largura, altura).
    :param max_tentativas: O número máximo de tentativas para encontrar a imagem.
    :param horizontal: O deslocamento horizontal para clicar após encontrar a imagem.
    :param vertical: O deslocamento vertical para clicar após encontrar a imagem.
    :param acao: A ação a ser executada quando a imagem for encontrada ('clicar' ou 'mover_mouse').
    """
    
    def clicar(x, y):
        pyautogui.click(x, y)

    def coordenada(x, y):
        print(f'Coordenadas da imagem: ({x}, {y})')

    def move_mouse(
        x,
        y,
        variationx=(-5, 5),
        variationy=(-5, 5),
        up_down=(0.2, 0.3),
        min_variation=-10,
        max_variation=10,
        use_every=4,
        sleeptime=(0.009, 0.019),
        linear=90,
    ):
        mkey.left_click_xy_natural(
            int(x) - random.randint(*variationx),
            int(y) - random.randint(*variationy),
            delay=random.uniform(*up_down),
            min_variation=min_variation,
            max_variation=max_variation,
            use_every=use_every,
            sleeptime=sleeptime,
            print_coords=True,
            percent=linear,
        )
    
    acoes_validas = ['clicar', 'mover_clicar']

    if acao not in acoes_validas:
        raise ValueError(f"Ação inválida: '{acao}'. Escolha entre {acoes_validas}.")

    tentativas = 0

    while tentativas < max_tentativas:
        tentativas += 1
        try:
            img = pyautogui.locateCenterOnScreen(nome_arquivo, confidence=confidence, region=region)
            if img:
                x, y = img
                x += horizontal
                y += vertical
                coordenada(x, y)
                if acao == 'clicar':
                    clicar(x, y)
                elif acao == 'mover_clicar':
                    move_mouse(x, y)
                return True
        except pyautogui.ImageNotFoundException:
            pass
        time.sleep(1)

    print(f'Imagem não encontrada após {max_tentativas} segundos.')
    return False

# Exemplo de uso
procurar_imagem('consultar.png', acao='mover_clicar')
