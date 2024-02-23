print("bienvenidos a la calculadora")
print("para salir escriba salir")
print("las operaciones son suma , resta, multiplicacion y division")

resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese numero:")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa siguiente  numero:")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print("operacion no valida")
        break
    print(f"el resultado de {resultado}")
