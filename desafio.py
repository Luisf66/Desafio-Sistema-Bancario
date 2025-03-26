saldo = 0
limite_transacao = 3
print(f'saldo inicial: R${saldo}')

while True:
    tipo = input('Digite o tipo da operação: ')

    if tipo == 'd':
        operacao = float(input('Digite o valor da operação: '))
        saldo = saldo + operacao
        print(f'saldo atual: R${saldo}')
    
    elif tipo == 's':
        operacao = float(input('Digite o valor da operação: '))
        if operacao > saldo:
            print('Saldo insuficiente.')
        elif operacao > 500:
            print('Limite de saque excedido.')
        elif limite_transacao == 0:
            print('Limite de transações excedido.')
        else:
            saldo = saldo - operacao
            limite_transacao -= 1
            print(f'saldo atual: R${saldo} transações restantes: {limite_transacao}')
    elif tipo == 'e':
        print(f'saldo atual: R${saldo}')
    elif tipo == 'b':
        break

print(f'saldo final: R${saldo}')