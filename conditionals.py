userReply = input("Você precisa enviar um pacote? (Enter sim or não) ")

if userReply == "sim": # Verifique se o usuário respondeu 'sim'
    print("Podemos ajudar você a enviar esse pacote!") # Se sim, imprima uma mensagem indicando ajuda para enviar o pacote
else:
    print("Volte sempre que precisar enviar um pacote. Obrigado.") # Caso contrário, imprima uma mensagem indicando que você deve retornar quando precisar enviar um pacote

userReply = input("Você gostaria de comprar selos, comprar um envelope ou fazer uma cópia? (Digite selos, envelope ou cópia) ") # Pergunte ao usuário se ele gostaria de comprar selos, comprar um envelope ou fazer uma cópia
if userReply == "selos": # Verifique se o usuário deseja comprar selos
    print("Temos muitos designs de selos para você escolher.") # Se sim, imprima uma mensagem indicando a disponibilidade de vários modelos de selos
elif userReply == "envelope": # Verifique se o usuário deseja comprar um envelope
    print("Temos muitos tamanhos de envelopes para você escolher.") # Se sim, imprima uma mensagem indicando a disponibilidade de vários tamanhos de envelope
elif userReply == "cópia": # Verifique se o usuário deseja fazer uma cópia
    copias = input("Quantas cópias você gostaria? (Digite um número) ") # Se sim, pergunte quantas cópias eles gostariam
    print("Aqui estão {} cópias.".format(copias)) # Imprima o número de cópias solicitadas
else:
    print("Obrigado, volte sempre.") # Se nenhuma das condições acima for atendida, imprima uma mensagem de agradecimento