#Cristobal Spinola
compradores_fortificados = set()
compradores_iluminados = set()
stock_fortificados = 500
stock_iluminados = 500
info_fortificados = {}
info_iluminados = {}

def comprarentrada_fortificados():
    global stock_fortificados
    if stock_fortificados <= 0:
        print("No quedan entradas disponibles para Los Fortificados.")
        return
    while True:
        nombrecomprador = input("Ingrese su nombre: ").strip()
        if not nombrecomprador:
            print("El nombre no puede estar vacío. Inténtelo de nuevo.")
            continue
        if len(nombrecomprador) < 3:
            print("El nombre debe tener al menos 3 caracteres. Inténtelo de nuevo.")
            continue
        if not all(part.isalpha() for part in nombrecomprador.split()):
            print("El nombre solo puede contener letras y espacios. Inténtelo de nuevo.")
            continue
        if len(nombrecomprador.split()) < 2:
            print("Debe ingresar al menos nombre y apellido. Inténtelo de nuevo.")
            continue
        if nombrecomprador.lower() in compradores_fortificados:
            print("El nombre ya ha comprado entrada para Los Fortificados.")
            return
        break
    while True:
        tipoentrada = input("Ingrese tipo de entrada (general(G), vip(V)): ").strip().upper()
        if tipoentrada not in ['G', 'V']:
            print("Tipo de entrada no válido. Debe ser 'G' o 'V'. Inténtelo de nuevo.")
            continue
        break
    while True:
        codigoconfirmacion = input("Ingrese el codigo de confirmacion: ").strip()
        if len(codigoconfirmacion) < 6:
            print("El código de confirmación debe tener al menos 6 caracteres. Inténtelo de nuevo.")
            continue
        if not any(c.isupper() for c in codigoconfirmacion):
            print("El código de confirmación debe tener al menos una letra mayúscula. Inténtelo de nuevo.")
            continue
        if not any(c.isdigit() for c in codigoconfirmacion):
            print("El código de confirmación debe tener al menos un número. Inténtelo de nuevo.")
            continue
        if any(c.isspace() for c in codigoconfirmacion):
            print("El código de confirmación no puede tener espacios en blanco. Inténtelo de nuevo.")
            continue
        break
    compradores_fortificados.add(nombrecomprador.lower())
    info_fortificados[nombrecomprador] = {
        "tipo": tipoentrada,
        "codigo": codigoconfirmacion
    }
    stock_fortificados -= 1
    print("Codigo de confirmación válido.")
    print(f"¡Entrada registrada con éxito para “los Fortificados”!")

def compraentrada_iluminados():
    global stock_iluminados
    if stock_iluminados <= 0:
        print("No quedan entradas disponibles para Los Iluminados.")
        return
    while True:
        nombrecomprador = input("Ingrese su nombre: ").strip()
        if not nombrecomprador:
            print("El nombre no puede estar vacío. Inténtelo de nuevo.")
            continue
        if len(nombrecomprador) < 3:
            print("El nombre debe tener al menos 3 caracteres. Inténtelo de nuevo.")
            continue
        if not all(part.isalpha() for part in nombrecomprador.split()):
            print("El nombre solo puede contener letras y espacios. Inténtelo de nuevo.")
            continue
        if len(nombrecomprador.split()) < 2:
            print("Debe ingresar al menos nombre y apellido. Inténtelo de nuevo.")
            continue
        if nombrecomprador.lower() in compradores_iluminados:
            print("El nombre ya ha comprado entrada para Los Iluminados.")
            return
        break
    while True:
        tipoentrada = input("Ingrese tipo de entrada (CV, PAL): ").strip().upper()
        if tipoentrada not in ['CV', 'PAL']:
            print("Tipo de entrada no válido. Debe ser 'CV' o 'PAL'. Inténtelo de nuevo.")
            continue
        break
    while True:
        codigoconfirmacion = input("Ingrese el codigo de confirmacion: ").strip()
        if len(codigoconfirmacion) < 5:
            print("El código de confirmación debe tener al menos 5 caracteres. Inténtelo de nuevo.")
            continue
        if sum(1 for c in codigoconfirmacion if c.isupper()) < 3:
            print("El código de confirmación debe tener al menos 3 letras mayúsculas. Inténtelo de nuevo.")
            continue
        if not any(c.isdigit() for c in codigoconfirmacion):
            print("El código de confirmación debe tener al menos un número. Inténtelo de nuevo.")
            continue
        if any(c.isspace() for c in codigoconfirmacion):
            print("El código de confirmación no puede tener espacios en blanco. Inténtelo de nuevo.")
            continue
        break
    compradores_iluminados.add(nombrecomprador.lower())
    info_iluminados[nombrecomprador] = {
        "tipo": tipoentrada,
        "codigo": codigoconfirmacion
    }
    stock_iluminados -= 1
    print("Codigo de confirmación válido.")
    print(f"¡Entrada registrada con éxito para “los Iluminados”!")

def entradasdisponibles():
    print("Entradas disponibles:")
    print(f"Los Fortificados: {stock_fortificados} entradas")
    print(f"Los Iluminados: {stock_iluminados} entradas")
    print("\nCompradores Los Fortificados:")
    if info_fortificados:
        for nombre, datos in info_fortificados.items():
            print(f"- {nombre} | Tipo: {datos['tipo']} | Código: {datos['codigo']}")
    else:
        print("  Sin compradores registrados.")
    print("\nCompradores Los Iluminados:")
    if info_iluminados:
        for nombre, datos in info_iluminados.items():
            print(f"- {nombre} | Tipo: {datos['tipo']} | Código: {datos['codigo']}")
    else:
        print("  Sin compradores registrados.")

def main():
    print("TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
    print("1. Comprar entrada Los Fortificados")
    print("2. Comprar entrada Los Iluminados")
    print("3. Stock de entradas disponibles para ambos conciertos")
    print("4. Salir")
    while True:
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            comprarentrada_fortificados()
        elif opcion == "2":
            compraentrada_iluminados()
        elif opcion == "3":
            entradasdisponibles()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")


main()