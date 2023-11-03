import datetime


saldo = 0
limite = float(500)
extrato_bancario = {
  'Extrato de Deposito': [], 'Extrato de Saque': [], 'Extrato Geral': []
}

numero_saques = 0

LIMITE_SAQUES = 3

data = datetime.datetime.now().strftime('%d/%m/%y %H:%M:%S') # data atual e hora

menu = """

----------------MENU---------------
      Selecione a opção desejada:
            1 = Depositar
            2 = Sacar
            3 = Extrato
            4 = Sair
            
  ==> """


while True:

  opcao = int(input(menu))

  if opcao == 1:

    print('\nDepósito')
    
    valor_deposito = float(input('Valor de deposito: R$ '))
    if valor_deposito > 0:
      saldo += valor_deposito
      extrato_bancario['Extrato de Deposito'].append(f'Data: {str(data)} - Deposito: R${valor_deposito:.2f}')
      extrato_bancario['Extrato Geral'].append(f'Data: {str(data)} - Deposito: R$ {valor_deposito:.2f}')

    else: 
      print('ERRO! Deposite valores acima de R$ 0')


  elif opcao == 2:

    print('\nSaque')

    if numero_saques < LIMITE_SAQUES:
      valor_saque = float(input('Valor de saque: R$: '))
      if valor_saque > saldo:
        print(f'\nSaldo insuficiente, seu saldo é de {saldo:.2f}')
      if valor_saque > 0:
        if valor_saque <= limite and valor_saque <= saldo:
          saldo -= valor_saque
          extrato_bancario['Extrato de Saque'].append(f'Data: {str(data)} - Saque: R${valor_saque:.2f}')
          extrato_bancario['Extrato Geral'].append(f'Data: {str(data)} - Saque R$ {valor_saque:.2f}')
          print('Saque Realizado com Sucesso!')
          numero_saques += 1
        else:
          print(f'\nO limite de saque é de {limite:.2f}')
      else:
        print('\nVocê deverá informar um valor de saque inválido')
    else:
      print('\nVocê não poderá efetuar o saque, você excedeu o limite diáriio de saque(3x)')
      
  elif opcao == 3:
    print('\nExtrato')

    while True:
      opcao_de_estrato = int(input("""
                                   
[ 1 ] Extrato Geral
[ 2 ] Extrato de Saques
[ 3 ] Extrato de Depósitos
[ 4 ] Sair 

==>"""))
      
      #if not extrato_deposito and extrato_saque or extrato_bancario: precisa de manutenção
       # print('Não foram realizadas movimentaçãoes.')

      if opcao_de_estrato == 1:
        for extrato_geral in extrato_bancario['Extrato Geral']:
          print('\nExtrato Geral')
          print(extrato_geral)
                
      elif opcao_de_estrato == 2:
        for extrato_saque in extrato_bancario['Extrato de Saque']:
          print('\nExtrato de Saque')
          print(extrato_saque)

      elif opcao_de_estrato == 3:
        for extrato_deposito in extrato_bancario['Extrato de Deposito']:
          print('\nExtrato de Depósito')
          print(extrato_deposito)

      elif opcao_de_estrato == 4:
        break

      print(f'Saldo atual:{saldo}')


  elif opcao == 4:
    break

  else:
    print('Operação inválida, por favor selecione novamente a operação desejada.')
print('Obrigado! e volte sempre')