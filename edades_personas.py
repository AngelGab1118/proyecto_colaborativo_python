# Lista de nombres
personas = ["Ana", "Luis", "Carlos", "Maria", "Pedro"]

# Diccionario con edades
edades = {
    "Ana": 30,
    "Luis": 25,
    "Carlos": 40,
    "Maria": 28,
    "Pedro": 35
}

# Solicitar nombre al usuario
nombre = input("Ingresa un nombre: ")

# Condicional para verificar si existe
if nombre in edades:
    print(nombre, "tiene", edades[nombre], "años.")
else:
    print("La persona no fue encontrada.")