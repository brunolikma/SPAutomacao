import Service, Nfe, Impressora
from tkinter import *

janela = Tk()
janela.title('SP_Sistema')
janela.geometry('305x305+700+300')
janela.configure(background='#D3D3D3')


def Tela_Fms_Service():
    label_fms_service = Label(janela, text='SERVICE', bg="white")
    label_fms_service.place(x=12, y=6, width=60, height=17)
    vertical1 = Label(janela, text='', bg="black")
    vertical1.place(x=4, y=4, width=2, height=300)
    vertical2 = Label(janela, text='', bg="black")
    vertical2.place(x=80, y=4, width=2, height=300)
    vertical3 = Label(janela, text='', bg="black")
    vertical3.place(x=156, y=4, width=2, height=300)
    vertical4 = Label(janela, text='', bg="black")
    vertical4.place(x=226, y=4, width=2, height=300)
    vertical4 = Label(janela, text='', bg="black")
    vertical4.place(x=302, y=4, width=2, height=300)
    horizontal1 = Label(janela, text='', bg="black")
    horizontal1.place(x=4, y=4, width=300, height=2)
    horizontal2 = Label(janela, text='', bg="black")
    horizontal2.place(x=4, y=155, width=300, height=2)
    horizontal3 = Label(janela, text='', bg="black")
    horizontal3.place(x=4, y=302, width=300, height=2)


    instalar = Button(janela, width=8, text='Instalar', command=Service.bt_instalar, bg="white")
    instalar.place(x=10, y=30)


    iniciar = Button(janela, width=8, text='Iniciar', command=Service.bt_iniciar, bg="white" )
    iniciar.place(x=10, y=60)


    parar = Button(janela, width=8, text='Parar', command=Service.bt_parar, bg="white")
    parar.place(x=10, y=90)


    desinstlar = Button(janela, width=8, text='Desinstalar', command=Service.bt_desinstalar, bg="white")
    desinstlar.place(x=10, y=120)

def Registra_Dll_Danfe():
    label_registra_danfe = Label(janela, text='DLL DANFE',bd=2, bg="white")
    label_registra_danfe.place(x=90, y=6, width=60, height=17)

    instalar = Button(janela, width=8, text='Instalar', command=Nfe.instalar_Nfe, bg="white")
    instalar.place(x=85, y=30)

    desinstalar = Button(janela, width=8, text='Desinstalar', command=Nfe.desinstalar_Nfe, bg="white")
    desinstalar.place(x=85, y=60)

def Impressora_Compartilha():
    label_impressora = Label(janela, text='Compartilha',bd=2, bg="white")
    label_impressora.place(x=158, y=6, width=67, height=17)
    compartilhar = Button(janela, width=7, text='EPSON', command=Impressora.Compartilhar_Impressora, bg="white")
    compartilhar.place(x=163, y=30)

Tela_Fms_Service()
Registra_Dll_Danfe()
Impressora_Compartilha()

janela.mainloop()


