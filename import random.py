import random
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
word = int(input("Esto es el creador de contraseñas, escribe la cantidad de simbolos que quieres para ella"))
idk = ""

for i in range(word):
    idk += random.choise(x)
print (idk)