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
        
        try:
            opcion = int(input("Selecciona una opción: "))
        except:
            print("❌ Debes ingresar un número válido")
            continue
            
        # 💰 Consultar saldo
        if opcion == 1:
            print(f"Tu saldo actual es: ${usuario['saldo']}")

        # ➕ Depositar
        elif opcion == 2:
            try:
                deposito = float(input("Ingrese monto a depositar: "))
                if deposito > 0:
                   usuario["saldo"] += deposito
                   usuario["movimientos"].append(f"Depósito: +${deposito}")
                   print("✅ Depósito realizado con éxito")
                   print(f"Saldo actual: ${usuario['saldo']}") 
                else:
                    print("❌ El monto debe ser positivo")
            except:
                print("❌ Entrada inválida")

        # ➖ Retirar
        elif opcion == 3:
            try:
                retiro = float(input("Ingrese monto a retirar: "))
                if retiro <= 0:
                     print("❌ El monto debe ser positivo")
                elif retiro <= usuario["saldo"]:
                    usuario["saldo"] -= retiro
                    usuario["movimientos"].append(f"Retiro: -${retiro}")
                    print("✅ Retiro realizado con éxito")
                else:
                     print("❌ Fondos insuficientes")
            except:
                print("❌ Entrada inválida")
                
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
