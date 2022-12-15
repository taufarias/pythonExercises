ano = int(input('Informe o ano: '))

if ano % 4 == 0:
  print('Ano bissexto!')
else:
    if ano % 4 == 0 and ano % 100 == 0:
        print('Não é ano bissexto!')
    else:
        if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
            print('Ano bissexto!')
        else:
            print('Não é ano bissexto!')