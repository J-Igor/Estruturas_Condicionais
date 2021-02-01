a = str(input("Olá, qual seu nome? "))
b = int(input("Digite a sua idade: "))
c = str(input("Digita o seu sexo (M/F): "))

altura = float(input("Digite sua altura (M): "))
peso = float(input("Digite seu peso (Kg): "))

imc = peso / altura**2
 
print("Seu IMC é: %.4f" % imc)
 
if imc < 16:
	print("Magreza extrema, consulte o seu nutricionista")
elif imc < 25:
	print("Parabens você está Saudável ")
elif imc < 35:
	print("Você está com Obesidade de Grau I ")
elif imc < 40:
	print("Você está com Obesidade de Grau II ")
else:
	print("Você está com Obesidade de Grau III ")