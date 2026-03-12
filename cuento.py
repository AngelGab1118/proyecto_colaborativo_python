def imprimir_cuento():
    """Imprime una historia sobre aprendizaje de Python y colaboración."""
    
    print("\n--- Cuento sobre aprender Python y trabajar en equipo ---\n")

    cuento = [
        "Había una vez un estudiante que estaba aprendiendo Python.",
        "Un día decidió trabajar con GitHub para colaborar con su equipo.",
        "Después de mucho esfuerzo lograron terminar su proyecto.",
        "Y aprendieron que trabajar en equipo hace el trabajo más fácil.",
        # >>> NUEVAS LINEAS AÑADIDAS <<<
        "El profesor reviso el repositorio y vio que cada miembro contribuyo.",
        "Esto les enseño la importancia de trabajar juntos y documentar su codigo."
    ]

    for linea in cuento:
        print(linea)

    print("\n--- Fin del cuento ---")


if __name__ == "__main__":
    imprimir_cuento()
