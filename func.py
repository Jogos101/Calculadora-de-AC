#Função para checar se o consumo > 130%media 
def prcnt(y, x):
  porcent = (y/x)*100
  if porcent > 130:
    return True
  else:
    return False

def teste(consumo, media):
  if consumo <= 5*media:
    return 1.5
  elif consumo <= 10*media:
    return 2
  else:
    return 3