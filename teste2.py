n = 100
n1 = 0
n2 = 1
lista = [0, 1]
numeroChecado = int(input("Qual numero você quer verificar se existe na sequência de FIBONACCI? "))

cont = 3
while cont <= n :
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
    lista.append(n3)

checarNumero = numeroChecado in lista 
if (checarNumero == True):
    print(f'O numero {numeroChecado} existe na sequência de Fibonacci')
else: 
    print(f'O numero {numeroChecado} não existe na sequência de Fibonacci')
