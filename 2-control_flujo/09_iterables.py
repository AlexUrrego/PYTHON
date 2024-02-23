# que son iterables ?
# Los iterables en Python son objetos que pueden ser iterados, es decir, sobre los cuales se puede loopar una sola vez para acceder a sus elementos. Ejemplos de iterables incluyen cadenas de texto, listas, tuplas, conjuntos, y diccionarios.
# En el contexto anterior, se mencionan varias funciones definidas en el módulo itertools de Python, el cual proporciona varias herramientas para trabajar con iterables. Algunas de las funciones mencionadas incluyen:
# accumulate(): retorna un iterador que produce valores acumulados de una función aplicada a los elementos de un iterable.
# chain(): retorna un iterador que produce los elementos de varios iterables en secuencia.
# compress(): retorna un iterador que produce los elementos de un iterable seleccionados por un iterador de booleanos.
# dropwhile(): retorna un iterador que descarta los elementos al principio de un iterable mientras una función dada devuelve True.
# filterfalse(): retorna un iterador con los elementos de un iterable que no satisfacen una función dada.
# groupby(): retorna un iterador con sub-iteradores agrupados según el valor de una función aplicada a los elementos.
# islice(): retorna un iterador con los elementos de un iterable seleccionados por un rango de índices.
# starmap(): retorna un iterador con los resultados de aplicar una función a los elementos de un iterable desempaquetado.
# takewhile(): retorna un iterador con los elementos al principio de un iterable mientras una función dada devuelve True.
# tee(): divide un iterador en varios iteradores independientes.
# zip_longest(): retorna un iterador con tuplas de los elementos correspondientes de varios iterables, completando con un valor dado si alguno de los iterables es más corto.
# Estas funciones permiten realizar operaciones más complejas sobre iterables de una manera fácil y eficiente.

# unos  ejemplos prácticos:

# 1. chain()
frutas = ['manzana', 'pera', 'platano']
vegetales = ['pimiento', 'calabaza', 'lechuga']
print(list(itertools.chain(frutas, vegetales)))
# ['manzana', 'pera', 'platano', 'pimiento', 'calabaza', 'lechiza']

# 2. filterfalse()


def es_verdadero(x): return len(x) > 5
