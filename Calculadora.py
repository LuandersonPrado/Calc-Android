#Titulo
titulo = 'calculadora imc'
titulo = titulo.upper()
print(titulo)

print('Qual o seu gênero?')

def genero():
    print("Escolha a opção abaixo:")
    print("Mulher[1]")
    print("Homen[2]")

def escolha():
    opcao = input("Escolha a opção: ")
    return opcao

genero()

opcao_escolhida = escolha()

if opcao_escolhida == '1':
    print('Mulher')
    altura = float(input('Insira sua altura: '))
    peso = float(input('Insira seu peso: '))

    imc = peso / (altura**2)

    #mulher
    if imc < 19:
        print('Abaixo do peso')
    elif 19 <= imc <= 23.9:
        print('Peso normal')
    elif 24 <= imc <= 28.9:
        print('Sobrepeso')
    elif 29 <= imc <= 33.9:
        print('Obesidade (Grau I)')
    elif 34 <= imc <= 38.9:
        print('Obesidade (Grau II)')
    elif imc > 39:
        print('Obsidade (Grau III)')
    else:
        print('Dados Incorretos')

elif opcao_escolhida == '2':
    print('Homen')
    altura = float(input('Insira sua altura: '))
    peso = float(input('Insira seu peso: '))

    imc = peso / (altura**2)

    #Homem
    if imc < 20:
        print('Abaixo do peso')
    elif 20 <= imc <= 24.9:
        print('Peso normal')
    elif 25 <= imc <= 29.9:
        print('Sobrepeso')
    elif 30 <= imc <= 34.9:
        print('Obesidade (Grau I)')
    elif 35 <= imc <= 39.9:
        print('Obesidade (Grau II)')
    elif imc > 40:
        print('Obsidade (Grau III)')
    else:
        print('Dados Incorretos')

else:
    print('Opção Inválida')
