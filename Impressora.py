import os, sys
import pyautogui as pag
import time

def Compartilhar_Impressora():
        epson_compartilhar = ('wmic printer where name="EPSON TM-T20X Receipt" set shared=TRUE , sharename = "EPSON"')
        os.popen(epson_compartilhar)
        epson_compartilhar = ('wmic printer where name="EPSON TM-T20 Receipt" set shared=TRUE , sharename = "EPSON"')
        os.popen(epson_compartilhar)

def Inicio_Instalacao():

    while True:
         instalar_impressoraT20 = ("C:\SP_IMPLANTACAO\Driver_T20\APD_510_T20.exe")
         os.system(instalar_impressoraT20)
         break

    while True:
        if pag.locateOnScreen('verificacao.png', confidence=0.9) or pag.locateOnScreen('verificacao2.png', confidence=0.9)\
        or pag.locateOnScreen('verificacao3.png', confidence=0.9):
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

    while  True:
        if  pag.locateOnScreen('verificaagree.png', confidence=0.9):
            click_agree = pag.locateCenterOnScreen('botaoagree.png', confidence=0.9)
            pag.click(click_agree)
            break
        else:
            print("Não Foi encontrado nada")

    while True:
        if pag.locateOnScreen('agreeselecionado.png', confidence=0.9):
            botao_agree = pag.locateCenterOnScreen('botaoinstall.png', confidence=0.9)
            pag.click(botao_agree)
            break
        else:
            print('Não Foi Localizado o Botao Install')

    while True:
        if pag.locateOnScreen('posinstalacao.png', confidence=0.9):
            botao_next2 = pag.locateCenterOnScreen("next2.png", confidence=0.8)
            pag.click(botao_next2)
            break
        else:
            print("Ainda nao localizei o Botao Next")

Inicio_Instalacao()
