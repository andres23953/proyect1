# Flujo automatizado de soporte
def flujo_soporte(opcion):
    if opcion == 1:
        return "Aquí tienes información sobre el producto A."
    elif opcion == 2:
        return "Aquí tienes información sobre el producto B."
    else:
        return "Opción no válida."

# Ejemplo de uso
opcion_usuario = int(input("Selecciona un producto: 1 o 2: "))
respuesta = flujo_soporte(opcion_usuario)
print(respuesta)
