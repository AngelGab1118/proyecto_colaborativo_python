import random

def jugar():
    print("🎮 Bienvenido al juego de adivinanza")

    # Elegir dificultad
    print("\nSelecciona dificultad:")
    print("1. Fácil (1-10)")
    print("2. Medio (1-20)")
    print("3. Difícil (1-50)")

    opcion = input("Elige una opción (1, 2 o 3): ")

    if opcion == "1":
        limite = 10
    elif opcion == "2":
        limite = 20
    elif opcion == "3":
        limite = 50
    else:
        print("Opción inválida, se usará nivel medio.")
        limite = 20

    numero_secreto = random.randint(1, limite)
    intentos = 5

    print(f"\nAdivina el número entre 1 y {limite}")
    print("Tienes 5 intentos")

    while intentos > 0:
        try:
            numero = int(input("Ingresa tu número: "))
        except:
            print("Por favor ingresa un número válido.")
            continue

        if numero == numero_secreto:
            print("🎉 ¡Correcto! Adivinaste el número.")
            return
        elif numero < numero_secreto:
            print("📉 El número es mayor.")
        else:
            print("📈 El número es menor.")

        intentos -= 1
        print(f"Te quedan {intentos} intentos\n")

    print(f"❌ Perdiste. El número era {numero_secreto}")


# Repetir juego
while True:
    jugar()
    repetir = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
    if repetir != "s":
        print("👋 Gracias por jugar")
        break