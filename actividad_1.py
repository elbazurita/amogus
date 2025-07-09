# 1. Crea una variable llamada `nombre` y asígnale tu nombre como string.
nombre = input("ingrese su nombre: ")

# 2. Imprime un saludo personalizado usando la variable `nombre`.
print("hola amigo", nombre)

# 3. Crea una variable `ciudad` con el nombre de tu ciudad.
ciudad = "palmira"
print(ciudad)

# 4. Imprime: "Hola, soy [nombre] y vivo en [ciudad]." 
print("hola soy", nombre, "y vivo en", ciudad)

# 5. Usa `input()` para pedirle al usuario su color favorito y guarda la respuesta en `color`.
color = input("ingrese su color: ")
print(color)

# 6. Imprime un mensaje que diga: "Tu color favorito es [color]." 
print("tu color favorito es", color)

# 7. Crea una variable `animal` y asígnale el string "gato". Luego, cambia su valor a "perro".
animal = "gato"
animal = "perro"
print(animal)

# 8. Concatena `nombre` y `ciudad` en una sola variable llamada `presentacion`. 
presentacion = "hola " + nombre + " y vivo en " + ciudad
print(presentacion)

# 9. Pide 4 datos al usuario, imprime resultado
nombre = input("ingrese su nombre: ")
apellido = input("ingrese su apellido: ")
telefono = input("ingrese su numero de telefono: ")
pais = input("ingrese un pais: ")

# 10. Pide 5 datos y has una operacion matematica
dato1 = float(input("Ingresa el primer número: "))
dato2 = float(input("Ingresa el segundo número: "))
dato3 = float(input("Ingresa el tercer número: "))
dato4 = float(input("Ingresa el cuarto número: "))
dato5 = float(input("Ingresa el quinto número: "))
suma_total = (dato1 + dato2 + dato3 + dato4 + dato5)
print("La suma de los 5 números es:", suma_total)

# 11. Crea dos variables `a = 5` y `b = 3`, y muestra su suma.
a = 5
b = 3
suma = (a + b)
print(suma)

# 12. Calcula la resta entre `a` y `b`
a = 5
b = 3
resta = (a - b)
print(resta)

# 13. Multiplica `a` por `b` y guarda el resultado en `multiplicacion`
a = 5
b = 3
multiplicacion = (a * b)
print(multiplicacion)

# 14.  Divide `a` entre `b` y muestra el resultado (asegúrate de obtener un número decimal)
a = 5
b = 3
divicion = (a / b)
print(divicion)

# 15. Eleva `a` a la potencia de `b`
a = 5
b = 3
potencia = (a ** b)
print(potencia)

# 16. Usa `input()` para pedirle al usuario su edad y guárdala como número entero
edad = int(input("ingrese su edad: "))
print(edad)

# 17. Suma 10 a la edad ingresada y muestra cuántos años tendrá en 10 años
edad2 = int(input("ingrese su edad: "))
suma = (edad2 + 10)
print("en 10 años tendras:", suma)

# 18. Pide dos números al usuario con `input()` y muestra su suma
numero = float(input("ingrese un numero: "))
numero2 = float(input("ingrese un numero: "))
suma1 = (numero + numero2)
print(suma1)

# 19. Calcula el módulo (residuo) de `a % b`
a = int(input("ingresa un numero: "))
b = int(input("ingresa un numero: "))
residuo = a % b
print(residuo)

# 20. Calcula el promedio de tres números enteros que ingrese el usuario
num = int(input("ingresa un numero: "))
num2 = int(input("ingresa un numero: "))
num3 = int(input("ingresa un numero: "))
promedio = (num + num2 + num3) / 3
print(promedio)

# 21. Pide al usuario su nombre completo y guarda la respuesta en `nombre_completo`
nombre_completo = input("ingrese su nombre completo: ")
print(nombre_completo)

# 22. Imprime solo el primer nombre (usa slicing o `.split()`)
primer_nombre = nombre_completo.split()[0]
print("tu primer nombre es:", primer_nombre)

# 23. Solicita al usuario dos números, luego imprime cuál es mayor
number = float(input("ingrese un numero: "))
number2 = float(input("ingrese un numero: "))
if number > number2:
    print("El número mayor es:", number)
elif number2 > number:
    print("El número mayor es:", number2)
else:
    print("Ambos números son iguales.")

# 24.  Pregunta al usuario su año de nacimiento y calcula su edad (usa el año actual manualmente, por ejemplo, 2025)
año_de_nacimiento = int(input("ingrese su año de nacimiento: "))
print(año_de_nacimiento)

# 25. Crea un mensaje que diga: "Hola [nombre], naciste en [año_nacimiento] y tienes [edad] años."
print(f"hola {nombre}, naciste en {año_de_nacimiento}, y tienes {edad} años.")

# 26. Usa `input()` para preguntar el nombre de una fruta, y responde con: "Me gusta la [fruta]"
fruta = input("ingresa el nombre de una fruta: ")
print(f"me gusta la {fruta}")

# 27. Pide dos números, muestra la suma, resta, multiplicación y división en un mismo bloque
numero8 = float(input("ingrese un numero: "))
numero9 = float(input("ingrese un numero: "))
suma2 = numero8 + numero9
resta3 = numero8 - numero9
multiplicacion3 = numero8 * numero9
division5 = numero8 / numero9
print(suma2, resta3, multiplicacion3, division5)