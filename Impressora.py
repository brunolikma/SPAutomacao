import os, sys
import pyautogui as pag
import time
import mouseinfo

def Compartilhar_Impressora():
    epson_compartilhar = ('wmic printer where name="EPSON TM-T20X Receipt" set shared=TRUE , sharename = "EPSON"')
    os.popen(epson_compartilhar)
    epson_compartilhar = ('wmic printer where name="EPSON TM-T20 Receipt" set shared=TRUE , sharename = "EPSON"')
    os.popen(epson_compartilhar)

def Inicio_Instalacao():
    os.system("C:\SP_IMPLANTACAO\Driver_T20\APD_510_T20.exe")

    while True:
        if pag.locateOnScreen('verificacao.png') or pag.locateOnScreen('verificacao2.png') or pag.locateOnScreen('verificacao3.png') :
            print("Seguindo para o proximo Passo")
            break
        else:
            time.sleep(2)
            print("Nao achei nada Aguardando...")

    while True:
        if pag.locateOnScreen('next.png', confidence=0.9) or pag.locateOnScreen('next2.png', confidence=0.9):
            botao_next = pag.locateCenterOnScreen("next2.png", confidence=0.8)
            pag.click(botao_next)
            break
        else:
            time.sleep(2)
            print("Nao O botao Next Aguardando...")

Inicio_Instalacao()