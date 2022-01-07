a = float(input("Escreva a nota 1: ")) 
b = float(input("Escreva a nota 2: "))
c = float(input("Escreva a nota 3: "))

media = (a + b + c)/3

print("A média das notas é: ", media)

if (media >= 7):
    print("Aprovado na disciplina!")
else:
    if (media >= 3 ):
        print("Exame!") 
    else:
        print("Reprovado na disciplina!")