def agregar_producto():
    print("agregar producto")
def actualizar_producto():
    print("actualizar producto")
def eliminar_producto():
    print("eliminar producto")
def buscar_producto():
    print("buscando producto")
def genera_informe():
    print("genera informe")

opcion_elegida=0

def muestra_menu():
    opcion_elegida = input("""Selecciona una opción:
      1. Agregar producto
      2. Actualizar producto
      3. Eliminar producto
      4. Buscar producto
      5. Genera informe de los productos existentes """)

    print(opcion_elegida)
    if(opcion_elegida == 1 or "1."):
        agregar_producto()
    elif (opcion_elegida == 2 or "2."):
        actualizar_producto()
    elif (opcion_elegida == 3 or "3."):
        eliminar_producto()
    elif (opcion_elegida == 4 or "4."):
        buscar_producto()
    elif (opcion_elegida == 5 or "5."):
        genera_informe()
    else:
        "Elige una opción válida, intentalo de nuevo"
        muestra_menu()


f = open("inventario.txt","r")
print(f.read())
f.close()

