
# Define la clase Producto
class Producto():

    stock = 0 # Atributo de clase no encapsulado
    
    # Método constructor con atrbutos nombre, precio y stock
    def __init__(self, nombre: str, precio: float, stock:int = 0):
        self.nombre = nombre.capitalize()
        self.precio = precio
        self.stock = stock # Si no se ingresa, tiene valor cero 

    # Método estático para validar una cantidad
    @staticmethod
    def validar_cantidad(cantidad :int):

        # Si la cantidad es negativa, retornará falso, de lo contrario verdadero
        return False if cantidad < 0 else True
        
    # Método que retorna los atributos del objeto de la clase
    @property
    def obtener_atributos(self):
        return self.nombre, self.precio, self.stock
    
    # Método para modificar el stock de un producto
    def modificar_stock(self, nuevo_stock :int):
        
        # Si es cantidad válida mayor que cero 
        if self.validar_cantidad(nuevo_stock):
            self.stock = nuevo_stock
        # De lo contrario retorna cero
        else:
            self.stock = 0

    # Suma los stocks de productos si tienen el mismo nombre
    def __add__(self, other):
        if self.nombre.lower() == other.nombre.lower():
            self.stock += other.stock
        return self
    
    # Resta los stocks de productos si tienen el mismo nombre
    def __sub__(self, other):
        if self.nombre == other.nombre:
            self.stock -= other.stock
        return self
    
    # Verifica igualdad entre productos de acuerdo con el nombre en minúsculas
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()


# Módulo de pruebas
if __name__ == "__main__":

    # Crea instancia del producto e imprime sus atributos por separado
    producto = Producto("aaa", 5000, 300)
    print(producto.nombre)
    print(producto.precio)
    print(producto.stock)            
    
    # Modifica el stock de la instancia e imprime los atributos
    producto.modificar_stock(-5)
    print(producto.obtener_atributos)

    # Crea 3 instancias de productos
    p1 = Producto("bbb", 3000)
    p2 = Producto("ccc", 4500)
    p3 = Producto("aaa", 4000, 100)

    # Modifica el stock de uno de ellos e imprime sus atributos (tupla)
    p2.modificar_stock(150)
    print(p2.obtener_atributos)

    # Imprime atributos de las instancias
    print(p1.obtener_atributos)
    print(p2.obtener_atributos)
    print(p3.obtener_atributos)

    # Suma de proroductos (stock)
    producto + p3
    print(producto.obtener_atributos)

    # Resta de productos (stock)
    producto - p3
    print(producto.obtener_atributos)

    # Compara nombres de productos
    print(p3 == producto)
    print(p2 == p1)
