palavra = input('Digite uma palavra e veja como ela fica de trás para frente: ')

def inverterString(texto):
    return texto[::-1]
    
print(inverterString(palavra))