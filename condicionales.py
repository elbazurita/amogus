#  1. verifica si un numero es positivo, negativo o cero.
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
edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("puede votar")
else:
    print("no puede votar")

# 8 aplica un descuento del 20% solo a clientes vip
total2 = float(input("Ingresa el total de la compra: "))
es_vip = input("¿Eres cliente VIP? (sí/no): ").lower()
if es_vip == "sí" or es_vip == "si":
    descuento = total2 * 0.20
    precio_final = total2 - descuento
    print("Eres cliente VIP. Se le aplica 20% de descuento.")
    print("El precio final es: $", precio_final)
elif es_vip == "no":
    print("No eres cliente VIP. No se aplica descuento.")
    print("El precio final es: $", total2)
else:
    print("Respuesta no válida. No se aplicó ningún descuento.")
    print("El precio final es: $", total2)

# 9.determina si un número es múltiplo de 5 y de 3 al mismo tiempo.
numero4 = int(input("ingresa un número: "))
if numero4 % 5 == 0 and numero4 % 3 == 0:
    print(f"{numero4} es múltiplo de 5 y 3")
else:
    print(f"{numero4} no es múltiplo de 5 y 3")

# 10.verifica si un número es divisible entre dos números dados.
numero5 = int(input("Ingresa el número que quieres verificar: "))
divisor1 = int(input("Ingresa el primer divisor: "))
divisor2 = int(input("Ingresa el segundo divisor: "))
if numero5 % divisor1 == 0 and numero5 % divisor2 == 0:
    print(f"{numero5} es divisible entre {divisor1} y {divisor2}.")
elif numero5 % divisor1 == 0:
    print(f"{numero5} solo es divisible entre {divisor1}.")
elif numero5 % divisor2 == 0:
    print(f"{numero5} solo es divisible entre {divisor2}.")
else:
    print(f"{numero5} no es divisible entre {divisor1} ni entre {divisor2}.")