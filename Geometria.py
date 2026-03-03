def controlador(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: entrada no válida. Por favor, ingrese un número entero.")

def menu():
    match figura:
        case 1:
            print("Has seleccionado Triángulo.")
        case 2:
            print("Has seleccionado Cuadrado.")
        case 3:
            print("Has seleccionado Círculo.")
        case 4:
            print("Has seleccionado Cubo.")
        case 5:
            print("Has seleccionado Pentagono.")
        case 6:
            print("Has seleccionado Rombo.")
        case 7:
            print("Has seleccionado Trapecio.")
        case 8:
            print("Has seleccionado Cilindro.")
        case 9:
            print("Has seleccionado Prisma.")
        case 10:
            print("Has seleccionado Cono.")
        case 11:
            print("---Hasta luego, has cerrado el programa.---")
            exit()
        case _:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

figura = controlador("Seleccione una figura geométrica:\n1. Triángulo\n2. Cuadrado\n3. Círculo\n4. Cubo\n5. Pentagono\n6. Rombo\n7. Trapecio\n8. Cilindro\n9. Prisma\n10. Cono\n11. Salir\n")
menu()