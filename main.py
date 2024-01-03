import func

media = 1
print("-"*39,"\n","Calculadora de alto consumo\n", "-"*39, sep='')

while media != 0:
  nimoveis = int(input("Informe o número de economias: "))
  if nimoveis == 0:
    break
  
  media = int(input("Informe o valor da média: "))
  if media*nimoveis < nimoveis*10:
    print("//ERRO//\n", "VALOR DO CONSUMO NÃO PODE SER MENOR QUE\nA TARIFA MÍNIMA DO IMÓVEL\n", sep='')
  else:
    consumo = int(input("Informe o valor do consumo: "))
    consumo = consumo//nimoveis
    mediaind = media//nimoveis
    porcentagem = func.prcnt(consumo, mediaind)
    if porcentagem == True and consumo >= 41:
      if nimoveis > 1:
        print("Media individual:", mediaind, "\nConsumo individual:", consumo)
        mod = func.teste(consumo, mediaind)
      else:
        mod = func.teste(consumo, media)

      nconsumo = mod * media
      print("Novo consumo: {:.0f}\n".format(nconsumo))
    else:
      print("Consumo fora da regra do AC.\n")

  print("-"*39,"\n","Novo cálculo de consumo\n", "-"*39, sep='')