buscar = 60
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrar", buscar)
        break
else:
    print("no se ha encontrado el numero")
