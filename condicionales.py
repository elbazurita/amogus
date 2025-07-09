'''#  1. verifica si un numero es positivo, negativo o cero.
numero1 = float(input("ingrese un numero: "))
if numero1 > 0:
    print(f"positivo porque es {numero1}")
elif numero1 < 0 :
    print(f"positivo porque es {numero1}")
else:
    print(f"es cero {numero1} ")

# 2. calcula el mayor de dos numeros ingresados._
n1 = float(input("ingrese un numero: "))
n2 = float(input("ingrese otro numero: "))
if n1 > n2:
    print(f"el numero mayor es {n1}")
elif n2 > n1:
    print(f"elnumero mayor es {n2}")
else:
    print("ambos numeros son iguales")

# 3. determina si un numero es par o impar.
numero = int(input("ingresa un numero: "))
if numero % 2 == 0:
    print("el numero es par")
elif numero % 2 != 0:
    print("el numero es impar")
else:
    print("no se pudo determinar si el numero es par o impar")

# 4. dado un numero, verifica si esta entre 10 y 20.
num = int(input("ingresa un numero: "))
if 10 <= num <= 20:
    print("el numero esta entre 10 y 20")
elif num < 10:
    print("el numero es menor que 10")
else:
    print("el numero es mayo que 20")

# 5. dados tres numeros encuentra el mayor usando condicionales.
num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))
num3 = int(input("ingresa el tercer numero: "))
if num1 >= num2 and num1 >= num3:
    print(f"el numero mayor es {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"el numero mayor es {num2}")
else:
    print(f"el numero mayor es {num3}")
'''
# 6. calcula el precio final con un 10% de descuento si el total es mayor a $100.
total = float(input("ingresa el total de la compra: "))
if total > 100:
    descuento = total * 0.10
    precio_final  = total - descuento
    print("se le dio un 10% de descuento")
elif total == 100:
    print("no se le dio el descuento")
    print(f"el precio final es {total}")
else:
    print("no se aplica descuento")
    print(f"el precio final es {total}")

# 7. verifica si una persona puede votar. (mayo o igual a 18 años).
