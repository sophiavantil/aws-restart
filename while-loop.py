import random

print("Bem-vindo ao Adivinhe o Número!")
print("As regras são simples. Vou pensar em um número e você tentará adivinhá-lo.")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Adivinhe um número entre 1 e 10: ")
    if int(guess) == number:
        print("Você adivinhou {}. Isso mesmo! Você venceu!".format(guess))
        isGuessRight = True
    else:
        print("Você adivinhou {}. Desculpe, não é isso. Tente novamente.".format(guess))