# -*- coding: utf-8 -*-

import telepot
import random
from datetime import datetime

token = '612013097:AAEDK1DfQ7f5XotEqyUAh1xWzL_t8q1aUeI'
bot = telepot.Bot(token) 

messagesDia = ["Bom dia gatão <3","Boooom diiia :3","Opa, bom dia amorzinho :3","Hoje estou de TPM, Tensão PROGRAMADA de Mulher rs te amo <3","Tenha um ótimo dia meu amor ^^","BOOOOOOOOOOOOOOM DIIIIIIIIIIIIIIIIIIIAAAAA ! hehe"]

messagesNoite = ["Boa noite meu lindo <3","Amooooooor! Boa noite hehe","BOOOOOAA NOITEEEEEEE <3","Dorme bem meu anjo :3 <3","Dorme bem, eu te amo <3","Nossa ! Essa lua tá linda igual você <3 haha","Um boa noite da sua Suzinha <3"]

idsMessage = []

now = datetime.now()

count = 0

horas_dia = 8
minutos_dia = 30

horas_noite = 22
minutos_noite = 9

def VerificarDia():
    global horas_dia
    global minutos_dia
    if now.hour == horas_dia and now.minute == minutos_dia:
        MandarMensagemGeral(random.choice(messagesDia))
        minutos_dia-=1
        
def VerificarNoite():
    global horas_noite
    global minutos_noite
    if now.hour == horas_noite and now.minute == minutos_noite:
        MandarMensagemGeral(random.choice(messagesNoite))
        minutos_noite-=1
        
      
def MandarMensagemGeral(msg):
    for r in idsMessage:
        print(r)
        bot.sendMessage(r, msg)

def MandarMensagem(idUser, msg):
    bot.sendMessage(idUser, msg)

def VerificarIdEmArray(resp):
        idUsuario = resp['message']['chat']['id']
        
        global idsMessage
        count = 0
        if idUsuario:
                for r in idsMessage:
                        if r == idUsuario: 
                                count += 1
                if count == 0:
                        idsMessage.append(idUsuario)
                        print(idUsuario)




def ReceberMensagem():
    resposta = bot.getUpdates()
    count =0
    if resposta:
            for r in resposta:
                VerificarIdEmArray(r)
    
        
VerificarIdEmArray(ReceberMensagem())

while True:
    VerificarDia()
    VerificarNoite()
    #VerificarIdEmArray(ReceberMensagem())
    
    
  