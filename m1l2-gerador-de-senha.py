import random

validacao_de_caracteres = "!@#$%¨&*()_+-=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567"
pedido_usuario = int(input('Digite o comprimento da senha:'))

senha_gerada = ""

for i in range(pedido_usuario):
    caractere_aleatorio = random.choice(validacao_de_caracteres)
    senha_gerada += caractere_aleatorio
    
print("Senha gerada:", senha_gerada)

