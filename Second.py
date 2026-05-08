nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? ")) 
# Convertir la entrada del usuario a un número entero

edad_el_proximo_ano = edad + 1

print("Hola,", nombre, "¡en un año tendrás", edad_el_proximo_ano, "años!")
#------------------------------------------------------------------------------------------------------------
palabrita = input("Ingresa una palabra: ").lower()
vocales = "aeiouáéíóú"
a=0
for letra in palabrita:
    if letra.lower() in "aeiouáéíóú":
        a += 1

print("Número de vocales:", a)
#------------------------------------------------------------------------------------------------------------
x = 5
x = x + 2
x *= 3
print(x)
