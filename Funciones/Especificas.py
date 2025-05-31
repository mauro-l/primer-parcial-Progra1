from Funciones.Generales import *


def cargar_nombres_participantes(array_nombres: list) -> bool:
    """Solicita al usuario que ingrese los nombres de los participantes y los almacena en la lista proporcionada.

    Args:
        array_nombres (list): Lista preexistente donde se almacenarán los nombres de los participantes. Debe tener una longitud mayor a cero.

    Returns:
        bool: True si los nombres fueron cargados correctamente en la lista, False si la lista no es válida o está vacía.
    """
    if not validar_array(array_nombres):
        # Si el array no es valido, se informa al usuario
        print("Error: Problemas con la lista de nombres.\n")
        return False

    for i in range(len(array_nombres)):
        # Se pide el dato a ingresar
        nombre = pedir_texto(
            f"Ingrese el nombre del participante {i + 1}: ", min_length=3
        )
        # Se guarda el dato en el array
        array_nombres[i] = nombre
    return True


def cargar_puntuaciones_jurado(matriz_puntuajes: list, array_nombres: list) -> bool:
    """Solicita al usuario que ingrese las puntuaciones de los jurados para cada participante y las almacena en la matriz proporcionada.

    Args:
        matriz_puntuajes (list): Matriz preexistente donde se almacenarán las puntuaciones de los jurados. Debe tener una longitud mayor a cero.
        array_nombres (list): Lista con los nombres de los participantes. Debe tener una longitud mayor a cero.

    Returns:
        bool: True si las puntuaciones fueron cargadas correctamente en la matriz, False si la matriz o la lista de nombres no son válidas o están vacías.
    """
    if not (validar_array(matriz_puntuajes) and validar_array(array_nombres)):
        print("Error: Problemas con los datos de participantes o puntuaciones.\n")
        return False

    for fil in range(len(matriz_puntuajes)):
        print(
            f"_____Cargando puntuajes del participante Nro {fil + 1} {array_nombres[fil]}_____"
        )
        for col in range(len(matriz_puntuajes[fil])):
            # Una vez dentro en la fila del participante, pedimos los puntuajes
            puntuacion = get_int(
                f"-> Ingrese el puntuaje del Jurado {col + 1}: ",
                f"-> Ingrese el puntuaje del Jurado {col + 1}: ",
                1,
                10,
            )
            matriz_puntuajes[fil][col] = puntuacion
    return True


def mostrar_puntuacion(
    matriz_puntuajes: list, array_nombres: list, indice: int
) -> bool:
    """
    Muestra por pantalla el nombre del participante y las puntuaciones de cada jurado para el participante indicado por el índice.

    Args:
        matriz_puntuajes (list): Matriz con las puntuaciones de los jurados para cada participante.
        array_nombres (list): Lista con los nombres de los participantes.
        indice (int): Índice del participante a mostrar.

    Returns:
        bool: True si se muestran correctamente las puntuaciones, False si hay error en los datos o el índice.
    """

    # Validaciones
    if not (validar_array(matriz_puntuajes) and validar_array(array_nombres)):
        print("Error: Problemas con los datos de participantes o puntuaciones.\n")
        return False

    if not (indice < len(array_nombres) and indice >= 0):
        print("Error: Índice de participante fuera de rango.\n")
        return False
    # Fin validaciones

    print(f"Participante Nro {indice + 1} {array_nombres[indice]}")
    print("==============================")

    for i in range(len(matriz_puntuajes[indice])):
        print(f"Puntuacion Jurado {i + 1}: {matriz_puntuajes[indice][i]}")

    return True


def mostrar_puntuaciones(matriz_puntuajes: list, array_nombres: list) -> bool:
    """
    Muestra por pantalla las puntuaciones y el promedio de todos los participantes.

    Para cada participante, muestra su nombre, las puntuaciones otorgadas por cada jurado
    (utilizando la función mostrar_puntuacion), la suma total de sus puntuaciones y su puntaje promedio.
    Separa visualmente cada participante.

    Args:
        matriz_puntuajes (list): Matriz con las puntuaciones de los jurados para cada participante.
        array_nombres (list): Lista con los nombres de los participantes.

    Returns:
        bool: True si se muestran correctamente todas las puntuaciones, False si hay error en los datos.
    """

    if not (validar_array(matriz_puntuajes) and validar_array(array_nombres)):
        print("Error: Problemas con los datos de participantes o puntuaciones.\n")
        return False

    for i in range(len(array_nombres)):
        print("______________________________")
        mostrar_puntuacion(matriz_puntuajes, array_nombres, i)
        suma_puntuacion = sumar_array(matriz_puntuajes, i)
        promedio = calcular_promedio(suma_puntuacion, len(matriz_puntuajes[i]))
        print(f"Puntaje Promedio: {promedio}/10")
    return True


def mostrar_participantes_promedio_menor(
    matriz_puntuajes: list, array_nombres: list, limite: float
) -> bool:
    """
    Muestra los participantes cuyo promedio de puntuaciones es menor al valor límite.

    Args:
        matriz_puntuajes (list): Matriz con las puntuaciones de los jurados para cada participante.
        array_nombres (list): Lista con los nombres de los participantes.
        limite (float): Valor límite para el promedio.

    Returns:
        bool: True si se muestran participantes, False si ninguno cumple la condición o hay error en los datos.
    """
    if not (validar_array(matriz_puntuajes) and validar_array(array_nombres)):
        print("Error: Problemas con los datos de participantes o puntuaciones.\n")
        return False

    encontrados = False
    for i in range(len(array_nombres)):
        suma = sumar_array(matriz_puntuajes, i)
        promedio = calcular_promedio(suma, len(matriz_puntuajes[i]))
        if promedio < limite:
            print(f"{i+1}) {array_nombres[i]} - Promedio: {promedio}")
            encontrados = True

    if not encontrados:
        print(f"No hay participantes con promedio menor a {limite}.")
        return False
    return True


def obtener_promedios_jurados(matriz_puntuajes: list) -> list:
    """
    Calcula y retorna una lista con el promedio de puntuaciones de cada jurado.

    Args:
        matriz_puntuajes (list): Matriz con las puntuaciones de los jurados para cada participante.

    Returns:
        list: Lista de promedios de cada jurado.
    """
    if not validar_array(matriz_puntuajes):
        return []

    cantidad_participantes = len(matriz_puntuajes)
    cantidad_jurados = len(matriz_puntuajes[0])
    promedios = []

    for col in range(cantidad_jurados):
        suma = 0
        for fil in range(cantidad_participantes):
            suma += matriz_puntuajes[fil][col]
        promedio = calcular_promedio(suma, cantidad_participantes)
        promedios.append(promedio)
    return promedios


# array_nombres = ["Ana", "Luis", "Pedro", "María", "Juan"]

# matrizVaciaDePrueba = [             # matrizdePrueba = [
#     [0, 0, 0],        # 0           #     [8, 5, 9],        #Participante 1
#     [0, 0, 0],        # 1           #     [5, 7, 6],        #Participante 2
#     [0, 0, 0],        # 2           #     [7, 4, 10],       #Participante 3
#     [0, 0, 0],        # 3           #     [6, 6, 8],        #Participante 4
#     [0, 0, 0],        # 4           #     [5, 6, 8]         #Participante 5
# ]                                   # ]
