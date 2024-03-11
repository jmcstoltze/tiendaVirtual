
# Importa las clases necesarias para ejecutar el programa
from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

# Importa time para el uso de sleep
import time

# Imprime título
print('''
        CREAR TIENDA
    -------------------------      
      ''')

# Almacenará el tipo de tienda seleccionada
tipo = 0

# Mientras no se seleccione un tipo adecuado el ciclo seguirá ejecutándose
while tipo not in (1, 2, 3):
     
    tipo = int(input('''    Ingrese tipo de tienda:
    ----------------------------------------------
        1. Restaurante
        2. Supermercado
        3. Farmacia \n\t
    '''))    

# Se solicita ingreso de nombre de tienda y costo de delivery
nombre = input('Ingrese nombre de la tienda: ')
costo = float(input('Ingrese costo de delivery: '))

# Dependiendo del tipo de tienda se crea la instancia correspondiente
if tipo == 1:
    tienda = Restaurante(nombre, costo)
elif tipo == 2:
    tienda = Supermercado(nombre, costo)
elif tipo == 3:
    tienda = Farmacia(nombre, costo)

# Imprime subtítulo
print('''
    Ingresar productos de la tienda
    -----------------------------------------------
      ''')

# Almacena la opción seleccionada por el usuario
opcion = "s"

# Ciclo que se ejecuta mientras el usuario no decida dejar de ingresar productos
while opcion == "s":
    
    # Se ingresa nombre y precio
    nombre = input('Ingrese nombre del producto: ')
    precio = float(input('Ingrese precio del producto: '))

    # Se inicializa el stock en cero
    stock = 0

    # Si la instancia de la tienda NO es un restaurante se solicita stock
    if not isinstance(tienda, Restaurante):
        stock = int(input('Ingrese stock: '))

    # Con los datos ingresados se crea instancia de un producto
    producto = Producto(nombre, precio, stock)

    # Se invoca la función para agregar el producto a la lista de la tienda
    tienda.ingresar_producto(producto)

    # Se pregunta si desea ingrsar más productos para detener o continuar con el ciclo
    print()
    opcion = input('¿Desea ingresar otro producto? (S/N): ').lower()
    print()

    # Si no se ingresa opción válida seguirá preguntando
    while opcion not in ("s", "n"):
        opcion = input('¿Desea ingresar otro producto? (S/N): ').lower()
        print()

print() # Salto de línea


# Variable para continuar o detener el siguiente ciclo
continuar = True

# El ciclo se ejecutar mientras el booleano sea True
while continuar:

    # Imprime lista de opciones
    print(''' 
            ¿Qué acción desea realizar?
        ------------------------------------------------  
          1. Listar los productos existentes
          2. Realizar una venta
          3. Salir del programa

        ''')
    
    # Recoje la opción ingresada por el usuario
    opcion = input("Ingrese opción \n")
    
    # Si la opción es 1 se listan los productos invocando la función
    if opcion == "1":
        print(tienda.listar_productos())
        time.sleep(3) # Breve pausa antes de continuar

    # Si la opción es 2 se procede con una venta
    elif opcion == "2":

        # Se solicita nombre y cantidad para la venta
        nombre = input('Ingrese nombre del producto: ')
        cantidad = int(input('Ingrese cantidad requerida: '))

        # Se invoca la función realizar venta de la tienda
        existe, cantidad_obtenida, precio_unitario, msj = tienda.realizar_venta(nombre, cantidad)

        # Si la tienda es un restaurante 
        if isinstance(tienda, Restaurante): 

            # El total a pagar será el precio por la cantidad solicitada
            total = precio_unitario * cantidad
            cantidad_obtenida = cantidad # La cantidad obtenidad será igual a la solicitada

        # Si se trata de un supermercado
        elif isinstance(tienda, Supermercado):

            # El total a pagar será el precio por la cantidad obtenida
            total = precio_unitario * cantidad_obtenida

        # Si se trata de una farmacia
        elif isinstance(tienda, Farmacia):

            # El total será el precio por la cantidad obtenida
            total = precio_unitario * cantidad_obtenida

            # Si no existe mensaje o la cantidad obtenida es diferente de cero
            if msj != "" and cantidad_obtenida != 0:
                
                # Imprime mensaje de máximo 3 unidades, advirtiendo
                print(f'\n\n{msj}\n\n')
                time.sleep(2)

        # Si existe el producto y suficiente stock para la venta
        if cantidad_obtenida != 0 and existe:

            # String con la impresión de la venta
            venta_string = f'''\n
                    Resumen venta
                --------------------------------------------------------------------------------
                {"PRODUCTO".ljust(30)}{"CANTIDAD".ljust(15)}{"PRECIO".ljust(15)}{"TOTAL".ljust(15)}
                --------------------------------------------------------------------------------                      
                {nombre.ljust(30)}{str(cantidad_obtenida).ljust(15)}{str(precio_unitario).ljust(15)}{str(total).ljust(15)}\n
                '''

            # Imprime el string
            print(venta_string)
            time.sleep(3) # Breve pausa antes de continuar
        
        # Si el producto no existe 
        elif not existe:

            # Indica que no existe el producto en la lista
            print(f"\n\n El producto {nombre} no está disponible en el listado \n\n ")
            time.sleep(3) # Breve pausa antes de continuar
        
        # Si la cantidad obtenida es igual a cero
        elif cantidad_obtenida == 0:

            # Indica que no existe stock para el producto
            print(f"\n\n Sin stock disponible para el producto {nombre} \n\n ")
            time.sleep(3) # Breve pausa antes de continuar

    # Opción para salir del programa
    elif opcion == "3":

        continuar = False # Se rompe el ciclo while
        print("¡Hasta pronto!") # Mensaje de despedida
        time.sleep(3)

    # Se imprime hasta que se ingrese una opción válida (1, 2, 3)
    else:
        print("Ingrese opción válida \n")
        time.sleep(1) #Breve pausa
