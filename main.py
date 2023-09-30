import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

c1="#0293F5"
c2="#006AFA"
c3="#0139E1"
c4="#0013FA"
c5="#1800F0"
c6="#FFFFFF"

janela=Tk()
janela.title("Classico")
janela.resizable(False,False)
largura_screen=janela.winfo_screenwidth()
altura_screen=janela.winfo_screenheight()
posx=largura_screen/2-260/2
posy=altura_screen/2-280/2
janela.geometry("%dx%d+%d+%d"%(260,280,posx,posy))

frameCima=Frame(janela,width=260,height=100,bg=c1,relief="raised")
frameCima.grid(row=0,column=0,sticky=NW)

frameBaixo=Frame(janela,width=260,height=300,bg=c2,relief="flat")
frameBaixo.grid(row=1,column=0,sticky=NW)

estilo=ttk.Style(janela)
estilo.theme_use("clam")

jogador=Label(frameCima,text="Você",height=1,font="TimesNewRoman 12 bold",bg=c1,fg=c6)
jogador.place(x=35,y=70)
jogadorLinha=Label(frameCima,height=100,bg=c1)
jogadorLinha.place(x=0,y=0)
jogadorPontos=Label(frameCima,text="0",height=1,font="TimesNewRoman 30 bold",bg=c1,fg=c6)
jogadorPontos.place(x=50,y=20)

SeparadorPontos=Label(frameCima,text=":",height=1,font="TimesNewRoman 30 bold",bg=c1,fg=c6)
SeparadorPontos.place(x=130,y=17)

PCPontos=Label(frameCima,text="0",height=1,font="TimesNewRoman 30 bold",bg=c1,fg=c6)
PCPontos.place(x=195,y=20)
PC=Label(frameCima,text="PC",height=1,font="TimesNewRoman 12 bold",bg=c1,fg=c6)
PC.place(x=205,y=70)
PCLinha=Label(frameCima,height=100, bg=c1)
PCLinha.place(x=255,y=0)

Empate=Label(frameCima,width=260,bg=c1)
Empate.place(x=0,y=95)

AparecePC=Label(frameCima,text="",height=1,font="TimesNewRoman 12 bold",bg=c1,fg=c6)
AparecePC.place(x=190,y=5)

ApareceUsuario=Label(frameCima,text="",height=1,font="TimesNewRoman 12 bold",bg=c1,fg=c6)
ApareceUsuario.place(x=35,y=5)

global voce
global pc
global rodadas
global pontos_voce
global pontos_pc

pontos_voce=0
pontos_pc=0
rodadas=5

def jogar(i):
    global rodadas
    global pontos_voce
    global pontos_pc
    if rodadas>0:
        pc=random.choice(['Pedra','Papel','Tesoura'])
        AparecePC['text']=pc
        voce=i
        ApareceUsuario['text']=voce
        
        if voce=='Pedra' and pc=='Pedra':
            jogadorLinha['bg']=c1
            PCLinha['bg']=c1
            Empate['bg']=c4
        elif voce=='Papel' and pc=='Papel':
            jogadorLinha['bg']=c1
            PCLinha['bg']=c1
            Empate['bg']=c4
        elif voce=='Tesoura' and pc=='Tesoura':
            jogadorLinha['bg']=c1
            PCLinha['bg']=c1
            Empate['bg']=c4
        elif voce=='Pedra' and pc=='Papel':
            jogadorLinha['bg']=c1
            PCLinha['bg']=c4
            Empate['bg']=c1
            pontos_pc+=10
        elif voce=='Pedra' and pc=='Tesoura':
            jogadorLinha['bg']=c4
            PCLinha['bg']=c1
            Empate['bg']=c1 
            pontos_voce+=10
        elif voce=='Papel' and pc=='Tesoura':
            jogadorLinha['bg']=c1
            PCLinha['bg']=c4
            Empate['bg']=c1
            pontos_pc+=10
        elif voce=='Tesoura' and pc=='Papel':
            jogadorLinha['bg']=c4
            PCLinha['bg']=c1
            Empate['bg']=c1
            pontos_voce+=10
        elif voce=='Tesoura' and pc=='Pedra':
            jogadorLinha['bg']=c1
            PCLinha['bg']=c4
            Empate['bg']=c1 
            pontos_pc+=10
        elif voce=='Papel' and pc=='Pedra':
            jogadorLinha['bg']=c4
            PCLinha['bg']=c1
            Empate['bg']=c1
            pontos_voce+=10
        PCPontos['text']=pontos_pc
        jogadorPontos['text']=pontos_voce
        rodadas-=1
    else:
        FimDoJogo()

def IniciarJogo():
    global Pedra
    global Papel
    global Tesoura
    global BotaoPedra
    global BotaoPapel
    global BotaoTesoura

    BotaoJogar.destroy()

    Pedra=Image.open("imagens/Pedra.png")
    Pedra=Pedra.resize((50,50),Image.ANTIALIAS)
    Pedra=ImageTk.PhotoImage(Pedra)
    BotaoPedra=Button(frameBaixo,command=lambda:jogar('Pedra'),width=50,image=Pedra,bg=c2,highlightbackground=c2,activebackground=c1,border=0)
    BotaoPedra.place(x=10,y=60)

    Papel=Image.open("imagens/Papel.png")
    Papel=Papel.resize((50,50),Image.ANTIALIAS)
    Papel=ImageTk.PhotoImage(Papel)
    BotaoPapel=Button(frameBaixo,command=lambda:jogar('Papel'),width=50,image=Papel,bg=c2,highlightbackground=c2,activebackground=c1,border=0)
    BotaoPapel.place(x=100,y=60)

    Tesoura=Image.open("imagens/Tesoura.png")
    Tesoura=Tesoura.resize((50,50),Image.ANTIALIAS)
    Tesoura=ImageTk.PhotoImage(Tesoura)
    BotaoTesoura=Button(frameBaixo,command=lambda:jogar('Tesoura'),width=50,image=Tesoura,bg=c2,highlightbackground=c2,activebackground=c1,border=0)
    BotaoTesoura.place(x=190,y=60)

def FimDoJogo():
    global rodadas
    global pontos_voce
    global pontos_pc
    
    pontos_voce=0
    pontos_pc=0
    rodadas=5
    
    BotaoPedra.destroy()
    BotaoPapel.destroy()
    BotaoTesoura.destroy()

    jogador_voce=int(jogadorPontos['text'])
    jogador_pc=int(PCPontos['text'])

    if jogador_voce>jogador_pc:
        Vencedor=Label(frameBaixo,text="Voce ganhou!!!",font="TimesNewRoman 12 bold",bg=c2,fg=c6)
        Vencedor.place(x=5,y=60)
    elif jogador_voce<jogador_pc:
        Vencedor=Label(frameBaixo,text="Voce Perdeu!!!",font="TimesNewRoman 12 bold",bg=c2,fg=c6)
        Vencedor.place(x=5,y=60)
    else:
        Vencedor=Label(frameBaixo,text="Foi um empate!!!",font="TimesNewRoman 12 bold",bg=c2,fg=c6)
        Vencedor.place(x=5,y=60)
    def JogarDenovo():
        jogadorPontos['text']='0'
        PCPontos['text']='0'
        Vencedor.destroy()
        BotaoJogarDenovo.destroy()
        IniciarJogo()
    BotaoJogarDenovo=Button(frameBaixo,command=JogarDenovo,width=30,border=0,text="Jogar denovo",highlightbackground=c2,activebackground=c1,activeforeground=c6,font="TimesNewRoman 10 bold",fg=c6,bg=c1)
    BotaoJogarDenovo.place(x=10,y=151)

BotaoJogar=Button(frameBaixo,command=IniciarJogo,width=30,border=0,text="Jogar",highlightbackground=c2,activebackground=c1,activeforeground=c6,font="TimesNewRoman 10 bold",fg=c6,bg=c1)
BotaoJogar.place(x=10,y=151)

janela.mainloop()