# src/app.py

# Inicializamos una lista vacía para almacenar los productos
products = []

# Función para listar los productos
def list_products():
    return products

# Función para agregar un nuevo producto
def add_product(name, qty):
    if not name:
        raise ValueError("name required")
    if qty < 0:
        raise ValueError("qty must be >= 0")
    products.append({"name": name, "qty": qty})
    return True
