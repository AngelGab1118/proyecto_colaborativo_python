# Base de datos de usuarios (PIN: saldo)
usuarios = {
    "1234": {"nombre": "Juan", "saldo": 1000, "movimientos": []},
    "5678": {"nombre": "Ana", "saldo": 1500, "movimientos": []}
}

print("💰 Bienvenido a tu Cajero Automático")

# 🔐 Login con PIN
pin = input("Ingrese su PIN: ")

if pin in usuarios:
    usuario = usuarios[pin]
    print(f"\nHola {usuario['nombre']} 👋")

    opcion = 0

    while opcion != 5:
        print("\n--- MENÚ ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Ver historial")
        print("5. Salir")

        opcion = int(input("Selecciona una opción: "))

        # 💰 Consultar saldo
        if opcion == 1:
            print(f"Tu saldo actual es: ${usuario['saldo']}")

        # ➕ Depositar
        elif opcion == 2:
            deposito = float(input("Ingrese monto a depositar: "))
            usuario["saldo"] += deposito
            usuario["movimientos"].append(f"Depósito: +${deposito}")
            print("Depósito realizado con éxito")

        # ➖ Retirar
        elif opcion == 3:
            retiro = float(input("Ingrese monto a retirar: "))
            if retiro <= usuario["saldo"]:
                usuario["saldo"] -= retiro
                usuario["movimientos"].append(f"Retiro: -${retiro}")
                print("Retiro realizado con éxito")
            else:
                print("❌ Fondos insuficientes")

        # 📜 Historial
        elif opcion == 4:
            print("\n--- HISTORIAL ---")
            if usuario["movimientos"]:
                for mov in usuario["movimientos"]:
                    print(mov)
            else:
                print("No hay movimientos")

        # 🚪 Salir
        elif opcion == 5:
            print("Gracias por usar el cajero 💳")

        else:
            print("❌ Opción inválida")

else:
    print("❌ PIN incorrecto")