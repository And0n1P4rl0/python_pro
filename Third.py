cadena = input("ingresa una cadena(O cualquier oración): ")

if len(cadena) > 10:
    resultado = cadena[:10] + "..."
else:
    resultado = cadena

print("Resultado: {}".format(resultado))
