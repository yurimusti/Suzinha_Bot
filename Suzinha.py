# -*- coding: utf-8 -*-

import telepot
from datetime import datetime

token = '612013097:AAEDK1DfQ7f5XotEqyUAh1xWzL_t8q1aUeI'
bot = telepot.Bot(token)

###########Definir aqui as técnicas para resposta automática#################
def Enviar_msg(id_user,msg):
    bot.sendMessage(id_user, msg)
    
#####################Recebendo Mensagens do Telegram########################
def Receber_msg(msg):

   ###########Id do 
   print(msg)
   id_usuario = msg['from']['id']
   ############Nome do Usuário
   Nome = (msg['from']['first_name'])
   
   if "boa noite" or "bom dia" in msg['text']:
       
       mensagem = 'Boa noite meu querido! Qual livro você gostaria de ler ?' 
       Enviar_msg(id_usuario,mensagem)
    
   if msg['text'] == 'TED':
       mensagem = 'Ótima escolha! Vou ver se temos ele no nosso sistema...' 
       Enviar_msg(id_usuario,mensagem)
       mensagem = 'Pronto! Ele não está disponivel, você tem preferência por outro livro ?'
       Enviar_msg(id_usuario,mensagem)
      
   if msg['text'] == 'TED2':
       mensagem = 'Já entendi. Tenho um disponivel, você gostaria de vir aqui entregar?'
       Enviar_msg(id_usuario,mensagem)
       
   if msg['text'] == 'sim':
       mensagem = 'Beleza! Vou te esperar aqui ' + Nome +'.'
       Enviar_msg(id_usuario,mensagem)
       
      
def MandarMensagem(msg):
    bot.sendMessage("671315312", msg)


now = datetime.now()
control = True


def VerificarData(i):
    if now.minute == 50 and now.hour == 20:
        MandarMensagem("Boa noite meu amor <3")
        i = 1
        print(now.minute)
    return i

while control:
  i=0
  i = VerificarData(i)
  if i > 0:
      print('Mandou boa noite.')
      control = False
  