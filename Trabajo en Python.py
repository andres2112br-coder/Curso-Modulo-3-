# Ejercicio 1 
print("=" * 40)
print("Ejercicio 1: Identificor de Paridad")
print("=" * 40)

numero = int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

# Ejercicio 2
print("\n" + "=" * 40)
print("Ejercicio 2: Sumatoria Acumalativa")
print("=" * 40)

limite = int(input("Ingrese el limite: "))
suma = 0

for i in range(1,limite + 1):
    suma += i

print(f"La suma de 1 hasta {limite} es: {suma}")

# Ejercicio 3
print("\n" + "=" * 40)
print("Ejercicio 3: Filtrado de Positivos")
print("=" * 40)

numeros = [ -5, 3, -1, 8, 0, -2, 7, 4, -9, 1]
positivos = []

print(f"Lista original: {numeros}")

for num in numeros:
    if num > 0:
        positivos.append(num)

print(f"Solo positivos: {positivos}")

#Ejercicio 4
print("\n" + "=" * 40)
print("Ejercicio 4: Contador de Vocales")
print("=" * 40)

frase = input("Ingrese una frase:")
vocales = "aeiouAEIOU"

contador = 0

for letra in frase:
    if letra in vocales:
        contador += 1

print(f"La frase tiene {contador} vocales.")

#Ejercicio 5
print("\n" + "=" * 40)
print("Ejercicio 5: Adivina el Numero")
print("=" * 40)

secreto = 7 
intento = 0

print("Adivina el numero secreto del 1 al 10")

while intento != secreto:
    intento = int(input("Tu intento:"))
    if intento != secreto:
        print("Incorrecto, PENDEJO INTENTA DE NUEVO :)")

print(f"Felicitaciones, No eres tan pendejo como esperaba el numero era el que estaba pensando {secreto}")

#Ejercicio 6
print("\n" + "=" * 40)
print("Ejercicio 6: Calculadora de Promedios")
print("=" * 40)

alumnos = {
    "Ana": 8.5,
    "Luis": 4.2,
    "Pedro": 9.8,
    "Maria": 7.1,
    "Carlos": 6.3,
    "Sofia": 8.9,
}

total = 0
aprobados = 0 

for nota in alumnos.values():
    total += nota
    if nota >= 6:
        aprobados += 1

promedio = total / len(alumnos)

print(f"Promedio general: {promedio:.2f}")
print(f"Alumnos aprobados(>=6): {aprobados} de {len(alumnos)}")

#Ejercicio 7
print("\n" + "=" * 40)
print("Ejercicio 7: Verificador de Primos")
print("=" * 40)

def es_primo(n):
    if n < 2:
        return False
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un numero para verificar si es primo o prima ;) : "))

if es_primo(numero):
    print(f"{numero} ES PRIMO :) ")
else:
    print(f"{numero} NO ES PRIMA :(")

#Ejercicio 8
print("\n" + "=" * 40)
print("Ejercicio 8:Interseccion de Datos")
print("=" * 40)

lista_a = [1, 2, 3, 4, 5, 6, 2, 3,]
lista_b = [4, 5, 6, 7, 8, 9, 4, 5,]

conjunto_a = set(lista_a)
conjunto_b = set(lista_b)
comunes = conjunto_a & conjunto_b

print(f"Lista A: {lista_a}")
print(f"Lista B: {lista_b}")
print(f"Elementos comunes: {comunes}")

#Ejercicio 9
print("\n" + "=" * 40)
print("Ejercicio 9: Tablas de Multiplicar")
print("=" * 40)

for tabla in range (1, 6):
    print(f"Tabla del {tabla}")
    for factor in range(1, 11):
        print(f"{tabla} x {factor} = {tabla * factor}")

#Ejercicio 10
print("\n" + "=" * 40)
print("Ejercicio 10:Clasificacion por Edades")
print("=" * 40)

personas = [
    ("Ana", 10),
    ("Luis", 25),
    ("Pedro", 80),
    ("Maria", 22),
    ("Carlos", 8),
    ("Sofia", 50),
]

for nombre , edad in personas:
    if edad < 18:
        categoria = "Menor"
    elif edad < 65:
        categoria = "Adulto"
    else:
        categoria = "Mayor"
    print(f"{nombre} ({edad} años) es {categoria}")


#Ejercicio 11
print("\n" + "=" * 40)
print("Ejercicio 11:Simulacion Bancaria")
print("=" * 40)

class BNC:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0: 
            self.saldo =+ monto
            print(f"Deposito de ${monto:.2f} exitoso. Fondo actual: ${self.saldo:.2f}")
        else:
            print("El monto a depositar debe ser positivo.")
    def retirar(self, monto):
        if monto <= 0:
            print("El monto a retirar debe ser positivo.")
        elif monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de ${monto:.2f} exitoso. Fondo actual: ${self.saldo:.2f}")
        else:
            print(f"Fondo Insuficiente. Fondos disponibles: ${self.saldo:.2f}")
    
    def ver_saldo(self):
        print(f"Titular: {self.titular} | Saldo: ${self.saldo:.2f}")


cuenta = BNC("Andres Barros", 1000)
cuenta.ver_saldo()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.retirar(2000)
cuenta.ver_saldo()

#Ejercicio 12
print("\n" + "=" * 40)
print("Ejercicio 12:Desplazamiento de Bits")
print("=" * 40)

numero = int(input("Ingrese un numero entero: "))

for desplazamiento, multiplicador in [(1, 2), (2, 4)]:
    resultado = numero << desplazamiento
    print (f"{numero} << {desplazamiento} = {resultado} (equivale a {numero} * {multiplicador})")

#Ejercicio 13
print("\n" + "=" * 40)
print("Ejercicio 13:Frecuencia de Palabras")
print("=" * 40)

parrafo = (
    "el sol brilla y el cielo es azul el sol es brillante"
    "y el cielo azul es hermoso y el sol siempre brilla"
)

print(f"Parrafo: {parrafo}")

palabras = parrafo.lower().split()
frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

for palabra, veces in sorted(frecuencia.items(), key=lambda x: -x[1]):
    print(f"'{palabra}' : {veces} vez/veces")
    

#Ejercicio 14
print("\n" + "=" * 40)
print("Ejercicio 14:SUcesion de Fibonacci")
print("=" * 40)

n = int(input("Cuantos terminos de fibonacci quieres generar?: "))

fibonacci = []

a, b = 0,1
while len(fibonacci) < n:
    fibonacci.append(a)
    a, b = b, a + b

print(f"Fibonacci ({n}terminos): {fibonacci}")

#Ejercico 15 
print("\n" + "=" * 40)
print("Ejercicio 15:")
print("=" * 40)

matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        resultado[i][j] = matriz_a[i][j] + matriz_b[i][j]

print("Matriz A:")
for fila in matriz_a:
    print(f"{fila}")

print("Matriz B:")
for fila in matriz_b:
    print(f"{fila}")

print("Resultado (A + B):")
for fila in resultado:
    print(f"{fila}")

print("\nFin del Programa")