import math  # libreria de py para  trabajar con numeros matematicos

print(round(3.6))  # numero mas  cercano a 3.6 redondeado
print(abs(-5))  # el valor absoluto de -5 es 5
# redondea hacia arriba, es decir, el mayor entero no menor que un número decimal
print(math.ceil(3.4))
# redondea hacia abajo,es decir ,el menor entero no mayor que un número decimal
print(math.floor(3.6))
# devuelve False porque 23 no es NaN (Not a Number),sino un número real.add()
print(math.isnan(23))
# La función pow() permite elevar un número a una potencia.
print(math.pow(2, 3))   # 2 elevado a la potencia de 3 =8
# La función sqrt() calcula la raíz cuadrada de un número.
print(math.sqrt(16))    # Raiz Cuadra de 16=4
# La función sin(), cos() y tan() permiten calcular funciones trigonométricas.
x = math.pi / 4
print(math.sin(x))     # seno de x
print(math.cos(x))     # coseno de x
print(math.tan(x))     # tangente de x
# La función asin(), acos(), atan() permiten calcular inversas trigonométricas.
y = math.sin(x)
print(math.asin(y))    # arcocoseno de y
z = math.cos(x)
print(math.acos(z))    # arcoseno de z
print(math.atan(0.5))  # arctangente de 0.5
# La función degrees() convierte grados en radianes y radians() los convierte en grados.
angle_radians = math.pi/2
angle_degrees = math.degrees(angle_radians)
print(f"{angle_degrees} grados")
angle_radians2 = math.radians(90)
angle_degrees2 = math.degrees(angle_radians2)
print(f"{angle_degrees2} radianes")
