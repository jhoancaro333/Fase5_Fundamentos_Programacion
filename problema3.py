
# Programa de reabastecimiento de inventario
# Problema 3 - Fase 5

# Matriz con la información de los artículos
inventario = [
    [101, "Teclado", 5, 15],
    [102, "Mouse", 20, 10],
    [103, "Monitor", 3, 8],
    [104, "Audifonos", 12, 12],
    [105, "Memoria USB", 4, 10]
]

# Funcion para calcular la cantidad a solicitar
def calcular_cantidad(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Mostrar el informe de inventario
print("======================================")
print("   INFORME DE REABASTECIMIENTO")
print("======================================")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_cantidad(stock_actual, stock_minimo)

    print("--------------------------------------")
    print("Codigo:", codigo)
    print("Articulo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock minimo:", stock_minimo)
    print("Cantidad a solicitar:", cantidad)

print("--------------------------------------")
print("Proceso finalizado correctamente.")
