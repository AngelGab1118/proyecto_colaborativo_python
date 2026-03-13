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

        # >>> NUEVAS LINEAS AÑADIDAS <<<
         "Es importante tener comunicación con tu equipo y compartir tu conocimiento para que todos puedan crecer juntos."
         "Con el tiempo descubrieron que cada miembro del equipo tenía habilidades diferentes.",
         "Mientras uno encontraba errores en el código, otro proponía nuevas ideas para mejorar el programa.",
         "Trabajar juntos les permitió aprender más rápido y resolver problemas con mayor facilidad.",

    ]

    for linea in cuento:
        print(linea)

    print("\n--- Fin del cuento ---")


if __name__ == "__main__":
    imprimir_cuento()
