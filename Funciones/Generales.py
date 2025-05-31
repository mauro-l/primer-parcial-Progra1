from Funciones.Validaciones import *


def crear_matriz(
    cantidad_filas: int, cantidad_columnas: int, valor_inicial: any
) -> list:
    """
    Crea y retorna una matriz (lista de listas) de tamaño cantidad_filas x cantidad_columnas,
    donde cada elemento está inicializado con valor_inicial.

    Args:
        cantidad_filas (int): Número de filas de la matriz.
        cantidad_columnas (int): Número de columnas de la matriz.
        valor_inicial (any): Valor con el que se inicializan todos los elementos de la matriz.

    Returns:
        list: Matriz creada como lista de listas.
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz += [fila]

    return matriz


def mostrar_matriz(matriz: list) -> None:
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            print(f"{matriz[fil][col]}", end=" ")
        print("")


def crear_array(cantidad_elementos: int, valor_inicial: any) -> list:
    """
    Crea y retorna una lista (array) de tamaño cantidad_elementos,
    donde cada elemento está inicializado con valor_inicial.

    Args:
        cantidad_elementos (int): Número de elementos del array.
        valor_inicial (any): Valor con el que se inicializan todos los elementos del array.

    Returns:
        list: Array creado como lista.
    """
    array = [valor_inicial] * cantidad_elementos
    return array


def mostrar_array(array: list) -> None:
    for i in range(len(array)):
        print(f"{array[i]}")


def sumar_array(matriz_numerica: list, indice_fila: int) -> int | float:
    """
    Suma todos los valores numéricos de una fila específica de una matriz numérica.

    Args:
        matriz_numerica (list): Matriz de números (lista de listas).
        indice_fila (int): Índice de la fila cuyos valores se desean sumar.

    Returns:
        int | float: Suma de los valores numéricos de la fila indicada.
    """
    suma_fila = 0
    for col in range(len(matriz_numerica[0])):
        if (
            type(matriz_numerica[indice_fila][col]) == int
            or type(matriz_numerica[indice_fila][col]) == float
        ):
            suma_fila += matriz_numerica[indice_fila][col]
    return suma_fila


def calcular_promedio(acumulador: float | int, contador: int) -> float | None:
    """
    Calcula el promedio a partir de un acumulador y un contador.

    Args:
        acumulador (float | int): Suma total de los valores.
        contador (int): Cantidad de elementos sumados.

    Returns:
        float | None: El promedio calculado, o None si el contador es cero.
    """
    if contador != 0:
        promedio = acumulador / contador
    else:
        promedio = None

    return promedio


def get_int(mensaje: str, mensaje_error: str, rango_min: int, rango_max: int) -> int:
    """
    Solicita al usuario un número entero dentro de un rango específico y lo retorna.

    Args:
        mensaje (str): Mensaje que se muestra al solicitar el número.
        rango_min (int): Valor mínimo aceptado.
        rango_max (int): Valor máximo aceptado.

    Returns:
        int: Número entero ingresado por el usuario dentro del rango especificado.
    """

    if not rango_min or not rango_max:
        print("Error: Los valores de rango no pueden ser nulos. (por ahora)")

    while True:
        opcion = input(mensaje)

        if not validar_entero(opcion):
            print(f"Error: '{opcion}' no es un número entero válido.\n")
            mensaje_error and print(mensaje_error)
            continue

        numero = int(opcion)
        if numero < rango_min or numero > rango_max:
            print(
                f"Error: '{numero}' se encuentra fuera del rango. ({rango_min} - {rango_max})"
            )
            continue

        return numero


def pedir_texto(mensaje: str, min_length=1, max_length=500) -> str:
    """
    Solicita al usuario un texto, valida su longitud y si solo debe contener letras y espacios.
    Args:
        mensaje (str): Mensaje a mostrar al usuario.
        min_length (int): Opcional | Longitud mínima, valor por defecto: 1.
        max_length (int): Opcional | Longitud máxima, valor por defecto 500.
    Returns:
        str: Texto ingresado válido.
    """
    while True:
        texto = input(mensaje + "\n")
        if len(texto) < min_length:
            print(f"Error: Debe tener al menos {min_length} caracteres\n")
            continue
        if len(texto) > max_length:
            print(f"Error: No puede tener más de {max_length} caracteres\n")
            continue
        if not validar_string(texto):
            continue
        return texto


def promedio_puntuaje_matriz(matriz_puntaje: list) -> list:
    """
    Calcula el promedio de puntaje de cada participante basado en las
    calificaciones de todos los jurados.

    Args:
        matriz_puntaje (list): Matriz con los puntajes de cada participante por jurado

    Returns:
        list: Array con el promedio de puntaje de cada participante
    """

    cantidad_filas = len(matriz_puntaje)
    promedio_puntaje_participantes = crear_array(cantidad_filas, None)

    for fil in range(len(matriz_puntaje)):
        contador = 0
        for col in range(len(matriz_puntaje[fil])):
            contador += matriz_puntaje[fil][col]
            promedio_puntaje_participantes[fil] = calcular_promedio(
                len(matriz_puntaje[fil]), contador
            )

    return promedio_puntaje_participantes
