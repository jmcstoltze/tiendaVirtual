
# Importación de la clase Producto desde el módulo producto
from producto import Producto

# Importación de la función abstractmethod
from abc import abstractmethod

 # Definición de la clase abstracta Tienda, que hereda de la clase ABC
class Tienda():

    # Constructor de la clase Tienda con parámetros
    def __init__(self, nombre: str, costo: float):

        self.nombre = nombre            # Nombre de la tienda
        self.costo_delivery = costo     # Costo del delivery
        self.productos = []             # Lista para almacenar los productos

    # Método para obtener los atributos de la tienda
    @property
    def obtener_atributos(self):

        # Retorna un tupla con los atributos de la clase
        return self.nombre, self.costo_delivery, self.productos
    
    # Método para ingresar un producto a la tienda
    def ingresar_producto(self, producto: Producto):
        
        if isinstance(self, Restaurante):

            # Establece en cero el stock, aunque se hayan ingresado valores
            producto.stock = 0

        elif isinstance(self, Farmacia) or isinstance(self, Supermercado):

            # Si el producto existe se suman los stocks
            for p in self.productos:
                if p == producto:
                    p += producto
        
        # Si no existe se agrega a la lista
        if producto not in self.productos:
            self.productos.append(producto)

    # Método abstracto para listar los productos de la lista
    @abstractmethod    
    def listar_productos():
        pass  

    # Método para la realización de una venta retorna la cantidad obtenida, el precio y un string
    def realizar_venta(self, nombre: str, cantidad: int = 0):

        cantidad_obtenida = 0       # Variables auxiliar para almacenar la cantidad solicitada o disponible
        precio_unitario = 0         # Variable auxiliar almacenar el precio del producto
        msj = ""                    # Mensaje que retornará la función
        existe = False              # Variable auxiliar para saber si el producto existe

        # Si es una farmacia se establece la cantidad máxima
        if isinstance(self, Farmacia):
            cantidad_max = 3 # Cantidad máxima que puede ser solicitada para un producto

            # Se itera la lista con los productos
            for p in self.productos:

                # se obtienen los atributos de cada objeto iterado
                nom, pre, stock = p.obtener_atributos    

                # Si se encuentra el producto y la cantidad solicitad es menor o igual al stock
                if nombre.lower() == nom.lower() and cantidad <= stock:
                    
                    # Se retorna la cantidad solicitada y el precio unitario
                    cantidad_obtenida = cantidad
                    precio_unitario = pre
                    
                    # Si la cantidad obtenida es mayor a la máxima solo se obtienen 3 unidades
                    if cantidad_obtenida > cantidad_max:
                        cantidad_obtenida = cantidad_max
                        # Mensaje alusivo
                        msj = "Máximo 3 unidades para el producto solicitado"
                    
                    # Se modifica el stock en el objeto
                    nuevo_stock = stock - cantidad_obtenida
                    p.modificar_stock(nuevo_stock)

                    # Producto existe y no es necesario seguir iterando
                    existe = True
                    break

                # Si el producto se encuentra pero la cantidad supera al stock
                elif nombre.lower() == nom.lower() and cantidad > stock:

                    # Se retorna el stock que queda disponible y el precio unitario
                    cantidad_obtenida = stock
                    precio_unitario = pre

                    # Si la cantidad obtenida es mayor a la máxima solo se obtienen 3 unidades
                    if cantidad_obtenida > cantidad_max:
                        cantidad_obtenida = cantidad_max
                        # Mensaje alusivo
                        msj = "Máximo 3 unidades para el producto solicitado"

                    # Se modifica el stock en el objeto
                    nuevo_stock = stock - cantidad_obtenida
                    p.modificar_stock(nuevo_stock)

                    # Producto existe y no es necesario seguir iterando
                    existe = True
                    break

        # Si se trata de un supermercado, trabajará con el stock
        elif isinstance(self, Supermercado):
            
            # Se itera la lista con los productos
            for p in self.productos:

                # se obtienen los atributos de cada objeto iterado
                nom, pre, stock = p.obtener_atributos    

                # Si se encuentra el producto y la cantidad solicitad es menor o igual al stock
                if nombre.lower() == nom.lower() and cantidad <= stock:
                    
                    # Se retorna la cantidadsolicitada y el precio unitario
                    cantidad_obtenida = cantidad
                    precio_unitario = pre
                    
                    # Se modifica el stock en el objeto
                    nuevo_stock = stock - cantidad
                    p.modificar_stock(nuevo_stock)

                    # Producto existe y no es necesario seguir iterando
                    existe = True
                    break

                # Si el producto se encuentra pero la cantidad supera al stock
                elif nombre.lower() == nom.lower() and cantidad > stock:

                    # Se retorna el stock que queda disponible y el precio unitario
                    cantidad_obtenida = stock
                    precio_unitario = pre

                    # Se modifica el stock en el objeto
                    nuevo_stock = stock - cantidad
                    p.modificar_stock(nuevo_stock)

                    # Producto existe y no es necesario seguir iterando
                    existe = True
                    break
        
        # Si es un restaurante solo verifica si el producto está disponible
        elif isinstance(self, Restaurante):

            # Itera la lista de productos para ver si existe
            for p in self.productos:
                nom, pre, stock = p.obtener_atributos

                if nombre.lower() == nom.lower():
                    
                    # Se retorna el precio
                    precio_unitario = pre

                    # Producto existe y no es necesario seguir iterando
                    existe = True
                    break


        # Devuelve la cantidad obtenida, el precio, si el pruducto existe y un mensaje para farmacia si corresponde
        return existe, cantidad_obtenida, precio_unitario, msj            

# Define la clase restaurante
class Restaurante(Tienda):

    # Método constructor con atributos nombre y costo de delivery
    def __init__(self, nombre: str, costo: float):

        # Llama al método constructor de la clase de la cual hereda
        super().__init__(nombre, costo)
    
    # Lista los productos de la tienda con nombre y precio
    def listar_productos(self):

        # Genera un string que se imprimirá en pantalla
        productos_str = f''' 
            Listado de Productos
        -------------------------------------------------------
        {"PRODUCTO".ljust(30)}{"PRECIO".ljust(15)}         
        -------------------------------------------------------         
        '''
        # Itera la lista para ir engrosando la string generada
        for p in self.productos:
            
            detalle_producto = p.obtener_atributos
            nombre, precio, stock = detalle_producto # Stock no se usará
            productos_str += f'{nombre.ljust(30)}{str(precio).ljust(15)}\n\t'

        # Devuelve la string con el listado
        return productos_str 

# Define la clase farmacia
class Farmacia(Tienda):

    # Método constructor con atributos nombre y costo de delivery
    def __init__(self, nombre: str, costo: float):
        
        # Llama al método constructor de la clase de la cual hereda
        super().__init__(nombre, costo)

    # Método que retorna un mensaje si el precio del producto es mayor a $15.000
    def mensaje_envio(self, precio: float):

        return "Envío gratis al solicitar este producto" if precio > 15000 else ""
    
    # Método para listar los productos ingresados en la lista de la tienda
    def listar_productos(self):

        # Genera string para imprimir en pantalla
        productos_str = f''' 
            Listado de Productos
        --------------------------------------------------------------------------------------
        {"PRODUCTO".ljust(30)}{"PRECIO".ljust(15)}         
        --------------------------------------------------------------------------------------
        '''
        # Itera la lista para ir engrosando el string
        for p in self.productos:
            
            # Invoca los atributos del producto
            detalle_producto = p.obtener_atributos
            nombre, precio, stock = detalle_producto # No se usa el stock
            msj = self.mensaje_envio(precio) # Se genera el mensaje predeterminado
            productos_str += f'{nombre.ljust(30)}{str(precio).ljust(15)}{msj}\n\t'

        # Devuelve el string
        return productos_str  

# Define clase supermercado y sus atributos
class Supermercado(Tienda):

    # Método constructor de la clase con nombre y costo de delivery
    def __init__(self, nombre: str, costo: float):

        # Invoca al método constructor de la clase de la cual hereda
        super().__init__(nombre, costo)
    
    # Método que retorna string con mensaje predeterminado
    def mensaje_stock(self, stock: int):

        # Si el stock es menor a 10 se retorna el mensaje
        return "Pocos productos disponibles" if 0 < stock < 10 else ""
    
    # Método para listar los productos de la tienda
    def listar_productos(self):

        # Genera una string con el listado de productos
        productos_str = f''' 
            Listado de Productos
        -----------------------------------------------------------------------------------------
        {"PRODUCTO".ljust(30)}{"PRECIO".ljust(15)}{"STOCK".ljust(15)}          
        -----------------------------------------------------------------------------------------         
        '''

        # Itera el listado para ir engrosando el string a imprimir
        for p in self.productos:
            
            detalle_producto = p.obtener_atributos      # Invoca los atributos
            nombre, precio, stock = detalle_producto    # Llama los atributos del producto
            msj = self.mensaje_stock(stock)             # Mensaje predeterminado
            productos_str += f'{nombre.ljust(30)}{str(precio).ljust(15)}{str(stock).ljust(15)}{msj}\n\t'

        # Devuelve el string con el listado
        return productos_str 

# Módulo de pruebas
if __name__ == "__main__":

    # Genera instancia de la tienda y muestra sus atributos
    t = Tienda("Donde Monchito", 300)
    print(t.obtener_atributos)

    # Genera instancia de restaurante
    r = Restaurante("Olguita Marina", 2500)
    # Crea instancia de productos
    producto1 = Producto("Pizza", 15990)
    producto2 = Producto("paeLLa", 19990)
    producto3 = Producto("Barros Luco", 8990, 150)
    producto4 = Producto("Pizza", 6000)
    # Los almacena en la lista del restaurante
    r.ingresar_producto(producto1)
    r.ingresar_producto(producto2)
    r.ingresar_producto(producto3)
    r.ingresar_producto(producto4)
    # Imprime el stock del producto 3
    print(producto3.stock)
    # Imprime el listado de productos
    print(r.listar_productos())

    # Genera instancia de un supermercado
    s = Supermercado("La Michi", 5600)
    # Crea instancia de productos
    producto1 = Producto("lechE", 2300, 5)
    producto2 = Producto("Arroz", 1990, 8)
    producto3 = Producto("Azúcar", 2300, -50)
    # IIngresa los productos al listado
    s.ingresar_producto(producto1)
    s.ingresar_producto(producto2)
    s.ingresar_producto(producto3)
    # Imprime listado
    print(s.listar_productos())

    # Crea instancia de farmacia
    f = Farmacia("Cruz Naranja", 3000)
    # Crea instancias de productos
    producto1 = Producto("aaa", 3000, 6)
    producto2 = Producto("bbb", 15500)
    producto3 = Producto("ccc", 8000)
    # Agrega productos al listado
    f.ingresar_producto(producto1)
    f.ingresar_producto(producto2)
    f.ingresar_producto(producto3)
    # Imprime el listado de los productos
    print(f.listar_productos())

    # Imprime los costos de delivery de cada tienda
    print(r.costo_delivery)
    print(s.costo_delivery)
    print(f.costo_delivery)

    # Realiza ventas con cada instancia
    print(r.realizar_venta("piZZa"))
    print(s.realizar_venta("arroz", 10))
    print(f.realizar_venta("AAA", 4))

    # Vuelve a listar los productos de las 3 tiendas
    print(r.listar_productos())
    print(s.listar_productos())
    print(f.listar_productos())
