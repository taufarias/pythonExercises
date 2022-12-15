import random

user_jogada = input('Escolha sua jogada (pedra, papel ou tesoura): ')

sorteio = random.randint (1, 3)

if sorteio == 1:
  sorteio = 'pedra'
else:
  if sorteio == 2:
    sorteio = 'papel'
  elif sorteio == 3:
    sorteio = 'tesoura'

if user_jogada ==  sorteio:
  print('"Empate!"')
elif user_jogada == 'pedra' and sorteio == 'tesoura' or user_jogada == 'papel' and sorteio == 'pedra' or user_jogada == 'tesoura' and sorteio == 'papel':
  print('"Você venceu!"')
else:
  print('"Você perdeu!"')
  
print(f'Jogada computador: {sorteio}')
  

