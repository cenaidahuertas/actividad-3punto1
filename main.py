from catalogo import Catalogo
from carrito import Carrito
from cliente import Cliente
from envio import Envio
from pedido import Pedido
from pago import Pago
from producto import Producto
from transportadora import Transportadora
from estadopedido import EstadoPedido as EstadoEnvio
from queja import Queja

def formatear_moneda(valor: float) -> str:
    """Formatea un valor numérico como moneda, agregando el símbolo de dólar y separadores de miles."""
    return "$" + format(int(valor), ",").replace(",", ".")

def crear_catalogo() -> Catalogo:
    """Crea un catálogo con productos de ejemplo."""
    catalogo = Catalogo()
    catalogo.agregar_producto(Producto("P001", "Laptop",  "Portatil para analisis de datos", 3500000, 5))
    catalogo.agregar_producto(Producto("P002", "Mouse",   "Mouse ergonomico inalambrico",      250000, 10))
    catalogo.agregar_producto(Producto("P003", "Teclado", "Teclado mecanico",                  346500, 8))
    catalogo.agregar_producto(Producto("P004", "Monitor", "Monitor Full HD de 24 pulgadas",    900000, 4))
    return catalogo

def registrar_cliente() -> Cliente:
    print("=== Registro de Cliente ===")
    nombre = input("Ingrese su nombre completo: ").strip()
    email = input("Ingrese su correo electrónico: ").strip()
    direccion = input("Ingrese su dirección de envío: ").strip()
    return Cliente(nombre, email, direccion)

def llenar_carrito(catalogo: Catalogo) -> Carrito:
    carrito = Carrito()
    while True:
        print("\n=== Catálogo de Productos ===")
        for producto in catalogo.listar_productos():
            print(f"{producto.codigo}: {producto.nombre} - {formatear_moneda(producto.precio)} (Stock: {producto.stock})")
        codigo = input("Ingrese el código del producto que desea agregar al carrito (o 'fin' para terminar): ").strip()
        if codigo.lower() == "fin":
            break
        producto = catalogo.obtener_producto(codigo)
        if producto is None:
            print("Producto no encontrado. Intente nuevamente.")
            continue
        cantidad_str = input(f"Ingrese la cantidad de '{producto.nombre}' que desea agregar: ").strip()
        if not cantidad_str.isdigit() or int(cantidad_str) <= 0:
            print("Cantidad inválida. Intente nuevamente.")
            continue
        cantidad = int(cantidad_str)
        if cantidad > producto.stock:
            print(f"No hay suficiente stock de '{producto.nombre}'. Stock disponible: {producto.stock}. Intente nuevamente.")
            continue
        carrito.agregar_producto(producto, cantidad)
        print(f"'{producto.nombre}' agregado al carrito.")
    return carrito

def realizar_pago() -> Pago:
    print("\n=== Información de Pago ===")
    while True:
        numero = input("Ingrese el número de su tarjeta de crédito (16 dígitos): ").strip()
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (MM/AA): ").strip()
        cvv = input("Ingrese el CVV (3 dígitos): ").strip()
        try:
            pago = Pago()
            pago.numero = numero
            pago.fecha_vencimiento = fecha_vencimiento
            pago.cvv = cvv
            return pago
        except ValueError as e:
            print(f"Error en la información de pago: {e}. Intente nuevamente.")

def registrar_queja(pedido: Pedido) -> Queja:
    print("\n=== Registro de Queja ===")
    motivo = input("Ingrese el motivo de su queja: ").strip()
    descripcion = input("Ingrese una descripción detallada de su queja: ").strip()
    return Queja(pedido, motivo, descripcion)

def main():
    catalogo = crear_catalogo()
    cliente = registrar_cliente()
    carrito = llenar_carrito(catalogo)
    if carrito.esta_vacio():
        print("No se han agregado productos al carrito. Saliendo del programa.")
        return
    pago = realizar_pago()
    envio = Envio("Transportadora XYZ", "123456789")
    pedido = Pedido(cliente, carrito, pago, envio)
    pedido.procesar_pedido()
    print("\n=== Resumen del Pedido ===")
    print(pedido)
    if pedido.estado == EstadoEnvio.COMPLETADO:
        print("\nEl pedido ha sido completado exitosamente.")
    else:
        print("\nEl pedido no pudo ser completado. Por favor, revise la información y vuelva a intentarlo.")
        queja = registrar_queja(pedido)
        print("\nGracias por registrar su queja. Nuestro equipo se pondrá en contacto con usted para resolver el problema.")
    
    if __name__ == "__main__":
        main()