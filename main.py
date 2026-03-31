from catalogo import Catalogo
from carrito import Carrito
from cliente import Cliente
from envio import Envio
from pedido import Pedido
from pago import Pago
from producto import Producto
from queja import Queja


def formatear_precio(valor):
    return "$" + format(int(valor), ",").replace(",", ".")


def crear_productos():
    productos = [
        Producto("P001", "Laptop", "Portatil para analisis de datos", 3500000, 5),
        Producto("P002", "Mouse", "Mouse ergonomico inalambrico", 250000, 10),
        Producto("P003", "Teclado", "Teclado mecanico", 346500, 8),
        Producto("P004", "Monitor", "Monitor Full HD de 24 pulgadas", 900000, 4),
    ]
    return Catalogo(productos)


def mostrar_productos(catalogo):
    print("\nCATALOGO DE PRODUCTOS")
    for producto in catalogo.productos:
        print(
            "Codigo:", producto.codigo,
            "| Nombre:", producto.nombre,
            "| Precio:", formatear_precio(producto.precio),
            "| Stock:", producto.cantidad_disponible
        )
        print("Descripcion:", producto.descripcion)


def pedir_cliente():
    print("REGISTRO DEL CLIENTE")
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    direccion = input("Direccion: ")
    return Cliente(nombre, correo, direccion)


def llenar_carrito(catalogo):
    carrito = Carrito()

    while True:
        mostrar_productos(catalogo)
        codigo = input("Ingrese codigo del producto o FIN: ").upper()

        if codigo == "FIN":
            break

        producto = catalogo.buscar_producto(codigo)

        if producto is None:
            print("Producto no encontrado.")
        else:
            cantidad = int(input("Cantidad: "))
            agregado = carrito.agregar_producto(producto, cantidad)

            if agregado:
                print("Producto agregado.")
            else:
                print("No se pudo agregar el producto.")

    return carrito


def mostrar_carrito(carrito):
    print("\nCARRITO")

    if len(carrito.productos) == 0:
        print("No hay productos.")
        return

    for producto in carrito.productos:
        print(producto.nombre, "-", formatear_precio(producto.precio))

    print("Total:", formatear_precio(carrito.calcular_total()))


def pedir_pago(total):
    print("\nPAGO")
    numero = input("Numero de tarjeta: ")
    fecha = input("Fecha de vencimiento: ")
    cvv = input("CVV: ")

    pago = Pago(numero, fecha, cvv)

    if pago.validar_pago(total):
        print("Pago exitoso.")
        return pago

    print("Pago no valido.")
    return None


def pedir_queja():
    respuesta = input("Desea registrar una queja? (si/no): ").lower()

    if respuesta == "si":
        descripcion = input("Escriba la queja: ")
        return Queja(descripcion)

    return None


def main():
    catalogo = crear_productos()
    cliente = pedir_cliente()
    carrito = llenar_carrito(catalogo)

    if len(carrito.productos) == 0:
        print("No se realizo el pedido.")
        return

    mostrar_carrito(carrito)
    pago = pedir_pago(carrito.total)

    if pago is None:
        return

    pedido = Pedido("PED001", cliente)
    pedido.productos = carrito.productos
    pedido.total = carrito.total
    pedido.estado = "CONFIRMADO"

    envio = Envio("Envios Colombia", 15000)

    print("\nRESUMEN FINAL")
    print("Cliente:", cliente.nombre)
    print("Correo:", cliente.correo)
    print("Direccion:", cliente.direccion)
    print("Total:", formatear_precio(pedido.total))
    print("Estado del pedido:", pedido.estado)
    print("Empresa de envio:", envio.empresa)
    print("Costo de envio:", formatear_precio(envio.costo))
    print("Estado del envio:", envio.estado)

    queja = pedir_queja()
    if queja is not None:
        print("Queja registrada:", queja.descripcion)


if __name__ == "__main__":
    main()
