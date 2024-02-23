# and, or, not
gas = True
encendido = True
edad = 18
if not gas and (encendido or edad > 17):
    print("puedes avanzar")

# que son operaciones de corto circuito ?
# En Python, las operaciones de cortocircuito son and y or, que funcionan de la siguiente manera:
# x and y: Devuelve x si este es falso, y de lo contrario devuelve y. En otras palabras,
# x es falso, entonces y no es evaluado en absoluto.
# x or y: Devuelve x si este es verdadero, y de lo contrario devuelve y. Si x es verdadero,
# entonces y no es evaluado en absoluto.
# Estas operaciones permiten al programador controlar el flujo de ejecución y evitar evaluar
# expresiones que no sean necesarias. Por ejemplo, en la expresión a and myfunc(b), si a es falso, entonces myfunc(b) no será llamada en absoluto. Esto puede ser útil para evitar errores de ejecución, como una división por cero o una desreferenciación de un puntero nulo.
# # Sin embargo, es importante tener en cuenta que estas operaciones pueden llevar a errores si
# no se utilizan correctamente. Por ejemplo, en la expresión expressionA and myfunc(b), si
# expressionA es falso y myfunc(b) tiene efectos secundarios, como asignar recursos al sistema,
# entonces myfunc(b) no será llamada y esto puede causar problemas.
# En general, es recomendable evitar usar efectos secundarios en las expresiones booleanas y
# utilizar valores con efectos secundarios en las evaluaciones. Esto ayudará a producir un código
# más claro y menos propenso a errores.
