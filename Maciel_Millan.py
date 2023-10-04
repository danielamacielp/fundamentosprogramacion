#Este programa calcula el área de un triángulo
#Primero defino base y altura como enteros y el resultado como real
base: int
altura: int
resultado: float
#Pido base y altura al usuario
base = int(input('Introduce la base del triángulo:'))
altura = int(input('Introduce la altura del triángulo:'))
#calculo el área del triángulo
resultado = float ((base*altura)/2)
#Le muestro el área del triángulo al usuario
print('El área del triángulo es', resultado)