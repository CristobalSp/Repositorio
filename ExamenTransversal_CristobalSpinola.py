#Cristobal Spinola
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'], 
                           }
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
              'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
              'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
                 }
def stock_marca(marca):
    total=0
    for modelo, datos in productos.items():
        if datos[0].lower()==marca.lower():
            total+=stock.get(modelo, [0,0]) [1]
    print(f"El stock total es ",{total})
def busqueda_ram_precio(p_min, p_max):
    #Solo pude hacer que imprima los modelos con un precio en un rango de precio minimo y precio maximo, no pude hacerlo funcionar con ram minima o maxima, pero funciona que es lo importante
    resultado=[]
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if p_min <= precio <= p_max and cantidad>0:
            marca=productos[modelo] [0]
            resultado.append(f"{marca}--{modelo}")
    if resultado:
        print(f"Los notebooks entre el rango de precios son ", sorted(resultado))
    else:
        print("No hay notebooks que mostrar.")
def eliminar_producto(modelo):
    while True:
        if modelo in stock and productos:
            productos.pop(modelo)
            stock.pop(modelo)
            print("Producto eliminado!!" )
        else:
            print("El modelo no exite!!")
        break
while True:
    print("Bienvenido a Pybooks")
    print("Ingrese una opcion:")
    print("1)Stock Marca")
    print("2)Busqueda por precio")
    print("3)Eliminar Producto")
    print("4)Salir")
    opcion=int(input("¿Que opcion desea?"))
    if opcion==1:
        marca=input("Ingrese marca a consultar: ")
        stock_marca(marca)
    elif opcion==2:
         while True:
            try:
                 p_min=int(input("Ingrese precio minimo: "))
                 p_max=int(input("Ingrese precio maximo: "))
                 break
            except ValueError:
                print("Debe ingresar valores enteros!!")
         busqueda_ram_precio(p_min, p_max)
    elif opcion==3:
         while True:
             modelo=input("Ingrese modelo a eliminar: ")
             eliminar_producto(modelo)
             eliminar=input("Desea eliminar otro producto?")
             if eliminar == "si":
                 continue
             elif eliminar == "no":
                 break
    elif opcion==4:
        print("Programa Terminado")
        break
    else:
        print("Debe seleccionar una opción válida!!")