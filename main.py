import random
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pregunta=int(input("Ingrese la longitud de la contraseña: "))
for i in range(pregunta):
    pregunta += random.choice(caracteres)
    print(f"La contraseña generada es: {pregunta}")