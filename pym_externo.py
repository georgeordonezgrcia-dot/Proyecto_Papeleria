class pym_externo:

  ruta_drive = "/content/drive/MyDrive/Curso SQL 202607/VentasPrueba.db"

  catalogo_precios_ajuste = {
    "Cuaderno profesional": 85.00,
    "Cuaderno doble raya": 65.00,
    "Lápiz del número 2": 8.00,
    "Pluma azul": 10.00,
    "Pluma negra": 10.00,
    "Pluma roja": 10.00,
    "Marcador permanente": 28.00,
    "Marcador para pizarrón": 35.00,
    "Resaltador amarillo": 22.00,
    "Resaltador verde": 22.00,
    "Resaltador rosa": 22.00,
    "Goma de borrar": 12.00,
    "Sacapuntas": 15.00,
    "Tijeras escolares": 35.00,
    "Tijeras de oficina": 75.00,
    "Regla de 30 cm": 18.00,
    "Compás metálico": 55.00,
    "Juego de geometría": 65.00,
    "Pegamento en barra": 25.00,
    "Pegamento líquido": 30.00,
    "Cinta adhesiva": 22.00,
    "Corrector líquido": 25.00,
    "Corrector en cinta": 38.00,
    "Carpeta tamaño carta": 45.00,
    "Carpeta tamaño oficio": 55.00,
    "Separadores de plástico": 40.00,
    "Hojas blancas tamaño carta": 120.00,
    "Hojas recicladas": 95.00,
    "Hojas cuadriculadas": 55.00,
    "Post-it": 45.00,
    "Bloc de notas": 35.00,
    "Engrapadora": 85.00,
    "Caja de grapas": 28.00,
    "Clips metálicos": 25.00,
    "Broches tipo baco": 30.00,
    "Folder manila": 8.00,
    "Folder plástico con broche": 25.00,
    "Archivador": 95.00,
    "Tóner para impresora": 850.00,
    "Cartuchos de tinta": 550.00,
    "Calculadora científica": 450.00,
    "Calculadora básica": 120.00,
    "Memoria USB": 180.00,
    "Mouse inalámbrico": 250.00,
    "Teclado": 350.00,
    "Agenda anual": 150.00,
    "Calendario de escritorio": 75.00,
    "Papel fotográfico": 180.00,
    "Papel bond": 140.00,
    "Cinta doble cara": 45.00,
    "Pega diamantina": 35.00
  }

  def generar_df_info_mejorada(
      fechaVenta,
      root_base_datos = ruta_drive,
      nombreTablaSql = "Consol_Ventas",
      r_o_a = "append",
      verbose=False
  ):
    """Simula la información de ventas diarias de una papelería grande
    y la almacena directamente en la base de datos SQL.

    Args:
        fechaVenta (str): Fecha de la venta en formato 'YYYY-MM-DD'.
        root_base_datos (str): Ruta de conexión de la base de datos sqlite.
        nombreTablaSql (str): Nombre de la tabla destino en la base de datos.
        r_o_a (str): Acción en caso de que exista la tabla ('append' o 'replace').
        verbose (bool): Si es True, imprime un mensaje de confirmación al finalizar.
    """
    import pandas as pd
    import random as r
    import sqlite3 as sql

    listaInsumosProductos = [
        "Cuaderno profesional", "Cuaderno doble raya", "Lápiz del número 2", "Pluma azul",
        "Pluma negra", "Pluma roja", "Marcador permanente", "Marcador para pizarrón",
        "Resaltador amarillo", "Resaltador verde", "Resaltador rosa", "Goma de borrar",
        "Sacapuntas", "Tijeras escolares", "Tijeras de oficina", "Regla de 30 cm",
        "Compás metálico", "Juego de geometría", "Pegamento en barra", "Pegamento líquido",
        "Cinta adhesiva", "Corrector líquido", "Corrector en cinta", "Carpeta tamaño carta",
        "Carpeta tamaño oficio", "Separadores de plástico", "Hojas blancas tamaño carta",
        "Hojas recicladas", "Hojas cuadriculadas", "Post-it", "Bloc de notas",
        "Engrapadora", "Caja de grapas", "Clips metálicos", "Broches tipo baco",
        "Folder manila", "Folder plástico con broche", "Archivador", "Tóner para impresora",
        "Cartuchos de tinta", "Calculadora científica", "Calculadora básica", "Memoria USB",
        "Mouse inalámbrico", "Teclado", "Agenda anual", "Calendario de escritorio",
        "Papel fotográfico", "Papel bond", "Cinta doble cara", "Pega diamantina"
    ]

    listaInsumosCajeros = [
        "Juan Carlos Ramírez López", "Miguel Ángel Torres Hernández", "José Luis González Cruz",
        "Carlos Alberto Mendoza Pérez", "Luis Fernando Ortega Díaz",
        "María Fernanda Castillo Reyes", "Ana Sofía Morales García", "Valeria Jiménez Flores",
        "Diana Carolina Salazar Ruiz", "Paola Alejandra Vargas León"
    ]

    listaInsumosSucursales = [
        "Centro Histórico", "Polanco", "Santa Fe", "Coyoacán", "Cuemanco",
        "Tlalpan", "Xochimilco", "La Condesa", "Reforma", "San Ángel"
    ]

    listaInsumoV_fecha = []
    listaInsumoV_cajero = []
    listaInsumoV_producto = []
    listaInsumoV_precio = []
    listaInsumoV_cantidad = []
    listaInsumoV_total = []
    listaInsumoV_sucursal = []

    for i in range(1, r.randint(1000, 35001)):
      cajero = r.choice(listaInsumosCajeros)
      producto = r.choice(listaInsumosProductos)
      
      # Precio obtenido del catálogo
      precio = pym_externo.catalogo_precios_ajuste[producto]
      # precio = round(r.randint(10, 20000) * r.random(), 2)
      
      cantidad = r.randint(1, 100)
      total = round(precio * cantidad, 2)
      sucursal = r.choice(listaInsumosSucursales)

      listaInsumoV_fecha.append(fechaVenta)
      listaInsumoV_cajero.append(cajero)
      listaInsumoV_producto.append(producto)
      listaInsumoV_precio.append(precio)
      listaInsumoV_cantidad.append(cantidad)
      listaInsumoV_total.append(total)
      listaInsumoV_sucursal.append(sucursal)

    dictPrevio = {
        "ColFecha": listaInsumoV_fecha,
        "ColCajero": listaInsumoV_cajero,
        "ColProducto": listaInsumoV_producto,
        "ColPrecio": listaInsumoV_precio,
        "ColCantidad": listaInsumoV_cantidad,
        "ColTotal": listaInsumoV_total,
        "ColSucursal": listaInsumoV_sucursal
    }

    df_ventas = pd.DataFrame(dictPrevio)

    conexion_sql = sql.connect(root_base_datos)
    df_ventas.to_sql(nombreTablaSql, conexion_sql, if_exists=r_o_a)
    conexion_sql.close()

    if verbose:
      print("Base de datos alimentada con éxito al", fechaVenta)

  def consulta(query, roorDb=ruta_drive):
    """Ejecuta una consulta SQL de tipo SELECT en la base de datos
    y retorna los resultados estructurados en un DataFrame de Pandas.

    Args:
        query (str): Código de la consulta SQL a ejecutar.
        roorDb (str): Ruta de conexión de la base de datos sqlite.

    Returns:
        pandas.DataFrame: Contenido de la consulta resultante.
    """
    import pandas as pd
    import random as r
    import sqlite3 as sql

    conexion = sql.connect(roorDb)
    df_consulta = pd.read_sql_query(query, conexion)
    conexion.close()
    return df_consulta

  def generar_df_info_rango(fechaInicial, fechaFinal, verbose=False):
    """Genera de manera secuencial la información de ventas diarias para
    un rango específico de fechas e introduce los registros en la base de datos.

    Args:
        fechaInicial (str): Fecha inicial del rango en formato 'YYYY-MM-DD'.
        fechaFinal (str): Fecha final del rango en formato 'YYYY-MM-DD'.
        verbose (bool): Si es True, muestra mensajes informativos del proceso.
    """
    import pandas as pd
    import random as r
    import sqlite3 as sql
    import datetime as dt

    def rangoFecha(fechaInicial, fechaFinal):
      rangoObjetosFecha = pd.date_range(start=fechaInicial, end=fechaFinal, freq="1d")
      rangoStrFecha = []
      for objFecha in rangoObjetosFecha:
        strFecha = dt.datetime.strftime(objFecha, "%Y-%m-%d")
        rangoStrFecha.append(strFecha)
      return rangoStrFecha

    rango_fechas = rangoFecha(fechaInicial, fechaFinal)

    for fechaVenta in rango_fechas:
      pym_externo.generar_df_info_mejorada(fechaVenta) # Se agrego "pym_externo."

    if verbose:
      print(f"Se generó con éxito las ventas del {fechaInicial} al {fechaFinal}")
