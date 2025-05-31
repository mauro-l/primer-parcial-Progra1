from Funciones.Generales import *
from Funciones.Validaciones import *
from Funciones.Especificas import *


# 6. Ver promedio de puntuaciones de cada jurado
def mostrar_promedio_por_jurado(matriz_puntuajes: list) -> bool:
    """
    Muestra el promedio de puntuaciones de cada jurado.

    Args:
        matriz_puntuajes (list): Matriz con las puntuaciones de los jurados para cada participante.

    Returns:
        bool: True si se muestran los promedios, False si hay error en los datos.
    """
    promedios = obtener_promedios_jurados(matriz_puntuajes)
    if not promedios:
        print("Error: No hay puntuaciones cargadas.")
        return False

    for i in range(len(promedios)):
        print(f"Jurado {i + 1}: Promedio = {promedios[i]:.2f}")
    return True


# 7. Mostrar al Jurado más estricto
def mostrar_jurados_mas_exigente(matriz_puntuajes: list) -> bool:
    """
    Muestra el jurado con la puntuación promedio más baja (más exigente).

    Args:
        matriz_puntuajes (list): Matriz con las puntuaciones de los jurados para cada participante.

    Returns:
        bool: True si se muestra el jurado más estricto, False si hay error en los datos.
    """
    promedios = obtener_promedios_jurados(matriz_puntuajes)
    if not promedios:
        print("Error: No hay puntuaciones cargadas.")
        return False

    menor_promedio = promedios[0]
    indice_jurado = 0
    for i in range(1, len(promedios)):
        if promedios[i] < menor_promedio:
            menor_promedio = promedios[i]
            indice_jurado = i
    print(
        f"El Jurado más estricto es el Jurado {indice_jurado + 1} con un promedio de {menor_promedio}"
    )
    return True


# 8. Mostrar al Jurado más generoso
def mostrar_jurado_mas_generoso(matriz_puntuajes: list) -> bool:
    """
    Muestra el jurado con la puntuación promedio más alta (menos exigente).

    Args:
        matriz_puntuajes (list): Matriz con las puntuaciones de los jurados para cada participante.

    Returns:
        bool: True si se muestra el jurado menos estricto, False si hay error en los datos.
    """
    promedios = obtener_promedios_jurados(matriz_puntuajes)
    if not promedios:
        print("Error: No hay puntuaciones cargadas.")
        return False

    mayor_promedio = promedios[0]
    indice_jurado = 0
    for i in range(1, len(promedios)):
        if promedios[i] > mayor_promedio:
            mayor_promedio = promedios[i]
            indice_jurado = i
    print(
        f"El Jurado mas generoso es el Jurado {indice_jurado + 1} con un promedio de {mayor_promedio:.2f}"
    )
    return True


# 10. Buscar participante por nombre
def buscar_participantes(array_nombres: list, matriz_puntuajes: list) -> bool:
    """
    Busca un participante por nombre exacto y muestra sus datos si existe.

    Args:
        array_nombres (list): Lista con los nombres de los participantes.
        matriz_puntuajes (list): Matriz con los puntajes de cada participante.

    Returns:
        bool: True si encontró el participante, False si no existe o hay error en los datos.
    """
    # Validación de datos
    if not (validar_array(matriz_puntuajes) and validar_array(array_nombres)):
        print("Error: Problemas con los datos de participantes o puntuaciones.\n")
        return False

    nombre_buscado = pedir_texto(
        "Ingrese el nombre del participante a buscar: ", min_length=3
    )
    for i in range(len(array_nombres)):
        if array_nombres[i] == nombre_buscado:
            print("Participante encontrado:")
            mostrar_puntuacion(matriz_puntuajes, array_nombres, i)
            return True
    print("Participante no encontrado")
    return False
