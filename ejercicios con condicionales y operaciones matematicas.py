# ejercicios con condicionales y operaciones matematicas

# 1. verifica si un numero es positivo, negativo o cero
numero = int(input("ingresa un numero: "))
if numero > 0:
    print("el numero es positivo")
elif numero < 0:
    print("el numero es negativo")
else:
    print("el numero es cero")

# 2. calcula el mayor de dos numeros ingresados
num = int(input("ingresa un numero: "))             
num1 = int(input("ingresa un numero: "))
if num >= num1:
    print(f"{num} es mayor que {num1}")
elif num1 >= num:
    print(f"{num1} es mayor que {num}")
else:
    print("no hay ningun numero ingresado")

# 3. determina si un numero es par o impar
num2 = int(input("ingresa un numero: "))
if num2 % 2 == 0:
    print("el numero es par")
else:("el numero es impar")

# 4. dado un numero verifica si esta entre 10 y 20
num3 = int(input("ingresa un numero: "))
if num3 >= 10 and num3 <= 20:
    print("el numero esta entre 10 y 20")
else:
    print("el numero no esta entre 10 y 20")

# 5. dados tres numeros encuentra el mayor usando condicionales
num4 = int(input("ingresa el primer numero: "))
num5 = int(input("ingresa el segundo numero: "))
num6 = int(input("ingresa el tercer numero: "))
if num4 >= num5 and num6:
    print("el primer numero es mayor")
elif num5 >= num4 and num6:
    print("el segundo numero es mayor")
elif num6 >= num4 and num5:
    print("el tercer numero es mayor")
else:
    print("no hay ningun numero ingresado")

# 6. calcula el precio final con un 10% de descuento si el total es mayor a $100
precio = float(input("ingresa un precio: "))
if precio > 100:
    descuento = precio * 0.10
    precio_total = precio - descuento
    print("se le dara un 10% de descuento")
else:
    precio_total = precio
    print("no se le da el descuento")
print(precio_total)

# 7. verifica si una persona puede votar (mayor o igual a 18 años)
edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("es mayor de edad, si puede votar")
else:
    print("no eres mayor de edad, asi que no puedes votar")

# 8. dado el precio y tipo de cliente (vip o normal), aplica un descuento del 20% solo a vip
cliente = input("ingresa el tipo de cliente (vip o normal): ")
precio1 = float(input("ingresa un precio: "))
if cliente == "normal":
    descuento = precio1
    precio1 = precio1
    print("no se le aplica descuento")
elif cliente == "vip":
    descuento = precio1 * 0.20
    print("se le aplica un 20% de descuento")
print(descuento)

# 9. determina si un numero es multiplo de 5 y de 3 al mismo tiempo
n = int(input("ingresa un numero: "))
if n % 3 == 0 and n % 5 == 0:
    print("es multiplo")
else:
    print("no es multiplo")

# 10. dado un numero verifica si es divisible entre dos numeros dados
n1 = int(input("ingresa un numero: "))
n2 = int(input("ingresa un numero: "))
n3 = int(input("ingresa un numero: "))
if n1 % n2 == 0 and n1 % n3 == 0:
    print("divisible")
else:
    print("no es divisible")
