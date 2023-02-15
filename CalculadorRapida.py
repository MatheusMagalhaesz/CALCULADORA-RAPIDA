num1 = float(input('Digite um número para realizar a operação: '))

opr = str(input('Escreva qual operação deseja realizar: '))

num2 = float(input('Agora digite o segundo número: '))

c1 = num1 + num2
c2 = num1 - num2
c3 = num1 * num2
c4 = num1 / num2 

if opr == '+':
    print('O resultado da Soma entre {} e {} resulta em: {}'.format(num1, num2, c1))

elif opr == '-':
    print('O resultado da Subtração entre {} e {} resulta em: {}'.format(num1, num2, c2))

elif opr == '*':
    print('O resultado da Multiplicação entre {} e {} resulta em: {}'.format(num1, num2, c3))

elif opr == '/':
    print('O resultado da Divisão entre {} e {} resulta em: {}'.format(num1, num2, c4))

else:
    print('Reinicie a operação inteira')
