produtos = [
    ['Chocolate', 5.12],
    ['Doritos', 15.25],
    ['Fandangos', 7.54],
]

pesquisa = 0

while pesquisa != 'sair':
  pesquisa = input('Informe o nome do produto ou digite "sair" para terminar: ')

  for item in produtos:
    if pesquisa in item:
      print('O preço do produto é: ', item[1])

if pesquisa == 'sair':
  print('Até mais!')


    



  

  