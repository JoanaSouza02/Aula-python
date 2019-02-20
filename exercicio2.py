nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))

if idade >= 18:
    print(f"Pode entrar no site {nome}")

elif idade < 11:
    print(f"Menor de idade, você ainda é criança {nome}")
elif idade > 11 < 18:
    print ("Menor de idade")