# -*- coding: utf-8 -*-

import telepot
from datetime import datetime

token = '612013097:AAEDK1DfQ7f5XotEqyUAh1xWzL_t8q1aUeI'
bot = telepot.Bot(token) 
      
def MandarMensagem(msg):
    bot.sendMessage("671315312", msg)


now = datetime.now()
control = True


def VerificarData(i):
    if now.minute == 50 and now.hour == 20:
        MandarMensagem("Boa noite meu amor ❤️️")
        i = 1
        print(now.minute)

    if now.hour == 7 and now.minute == 30:
        MandarMensagem("Bom dia meu lindo ❤️️")

    return i

while control:
  i=0
  i = VerificarData(i)
  if i > 0:
      print('Mandou boa noite.')
      i=0
      
  