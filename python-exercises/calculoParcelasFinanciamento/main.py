financiamento = float(input('Digite o valor do empréstimo: '))
i = float(input('Digite a taxa de juros: '))
t = int(input('Prazo para pagamento: '))

i = i/100

amortizacao = financiamento / t
devedor = financiamento

for contador in range(1, t+1): 
  juros = devedor * i
  parcela = amortizacao + juros
  devedor -= amortizacao
  print(f'Parcela {contador} | J: {juros:.2f} | A: {amortizacao:.2f} | Pgto: {parcela:.2f} | Deve: {devedor:.2f}')