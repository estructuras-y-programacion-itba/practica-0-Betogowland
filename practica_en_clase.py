class producto:
    
    tasa_impuesto: 0.16

    def __init__(self,nombre,precio):
        producto.validar_precio(precio)
        self.nombre=nombre
        self.precio= precio
        
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio}"

    def __gt__(self, otro):
        if not (isinstance(otro, producto)):
            return False
        
        return self.precio >otro.get_precio()
    

    @staticmethod
    def validar_precio(precio):
        if type(precio) != int and precio < 0 and type(precio) != float:
            raise ValueError("El precio debe ser un numero entero mayor a 0")
        
    @classmethod
    def actualizar_tasa(cls,tasa_nueva):
        cls.tasa_impuesto = tasa_nueva    
        
    def calcular_precio_con_impuesto(self):
        return self.precio * (1 + producto.tasa_impuesto)
         
class producto_perecedero(producto):
    def __init__(self, nombre, precio, fecha_vencimiento):
        super().__init__(nombre, precio)
        self.fecha_vencimiento = fecha_vencimiento
        
prod1 = producto('Notebook', 1000)
print(prod1)