from catalogo import Catalogo
from carrito import Carrito
from cliente import Cliente
from envio import Envio
from pedido import Pedido
from pago import Pago, PagoTarjeta
from producto import Producto
from transportadora import Transportadora
from estadopedido import EstadoPedido
from queja import Queja


def formatear_precio(valor: float) -> str:
    return "$" + format(int(valor), ",").replace(",", ".")


def crear_catalogo() -> Catalogo:
    productos = [
        Producto("P001", "Laptop",  "Portatil para analisis de datos", 3500000, 5),
        Producto("P002", "Mouse",   "Mouse ergonomico inalambrico",      250000, 10),
        Producto("P003", "Teclado", "Teclado mecanico",                  346500, 8),
        Producto("P004", "Monitor", "Monitor Full HD de 24 pulgadas",    900000, 4),
    ]
    return Catalogo(productos)


def registrar_cliente() -> Cliente:
    print("\n=== Registro de Cliente ===")
    nombre    = input("Nombre   : ").strip()
    correo    = input("Correo   : ").strip()
    direccion = input("Dirección: ").strip()
    return Cliente(nombre, correo, direccion)


def llenar_carrito(cliente: Cliente, catalogo: Catalogo) -> Carrito:
    carrito = cliente.crear_carrito()

    while True:
        cliente.ver_catalogo(catalogo)
        codigo = input("\nCódigo del producto (o FIN para terminar): ").upper().strip()

        if codigo == "FIN":
            break

        producto = catalogo.buscar_producto(codigo)
        if producto is None:
            print("✗ Producto no encontrado.")
            continue

        try:
            cantidad = int(input("Cantidad: "))
            if carrito.agregar_producto(producto, cantidad):
                print("✓ Producto agregado.")
            else:
                print("✗ No se pudo agregar el producto.")
        except ValueError as e:
            print(f"Error: {e}")

    return carrito


def realizar_pago(total: float) -> Pago | None:
    print("\n=== Información de Pago ===")
    while True:
        numero = input("Número de tarjeta (16 dígitos): ").strip()
        fecha  = input("Fecha de vencimiento (MM/AA)  : ").strip()
        cvv    = input("CVV (3 dígitos)               : ").strip()
        try:
            pago = PagoTarjeta(numero, fecha, cvv)
            if pago.procesar_pago(total):
                print("✓ Pago procesado exitosamente.")
                return pago
            print("✗ Pago no válido.")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}. Intente nuevamente.")


def registrar_queja(cliente: Cliente) -> None:
    respuesta = input("\n¿Desea registrar una queja? (si/no): ").strip().lower()
    if respuesta == "si":
        descripcion = input("Escriba su queja: ").strip()
        queja = Queja(
            id="Q001",
            cliente=cliente.nombre,
            descripcion=descripcion
        )
        queja.registrar_queja()
        print(cliente.presentar_queja(queja.descripcion))


def main() -> None:

    # 1. Catálogo
    catalogo = crear_catalogo()

    # 2. Cliente
    cliente = registrar_cliente()

    # 3. Carrito
    carrito = llenar_carrito(cliente, catalogo)

    if not carrito.productos_seleccionados:
        print("\n✗ Carrito vacío. No se realizó el pedido.")
        return

    print(str(carrito))

    # 4. Pago
    pago = realizar_pago(carrito.total)
    if pago is None:
        return

    # 5. Pedido
    pedido = Pedido(
    id_pedido="PED001",
    cliente=cliente,
    total=carrito.total,
    estado=EstadoPedido.CONFIRMADO
)
    pedido.cambiar_estado(EstadoPedido.CONFIRMADO)

    # 6. Transportadora y Envío
    transportadora = Transportadora(
        nombre="Envíos Colombia",
        costo_envio=15000,
        tiempo_entrega=3
    )
    envio = Envio(
        pedido=pedido,
        empresa_transportadora=transportadora,
        estado=EstadoPedido.PENDIENTE
    )
    envio.despachar()

    # 7. Resumen final
    print("\n=== RESUMEN FINAL ===")
    print(str(cliente))
    print(f"\nTotal pedido   : {formatear_precio(pedido.total)}")
    print(f"Estado pedido  : {pedido.estado.value}")
    print(str(envio))
    print(f"Costo de envío : {formatear_precio(transportadora.costo_envio)}")
    print(f"Tiempo entrega : {transportadora.tiempo_entrega} días")

    # 8. Queja
    registrar_queja(cliente)


if __name__ == "__main__":
    main()

