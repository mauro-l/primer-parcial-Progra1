import os
from Funciones.Generales import *
from Funciones.Validaciones import *
from Funciones.Especificas import *
from inputs import *

cantidad_participantes = 5
cantidad_jurados = 3

array_nombres = crear_array(cantidad_participantes, None)
promedio_puntuaje_jurado = crear_array(cantidad_jurados, None)
matriz_puntuajes = crear_matriz(cantidad_participantes, cantidad_jurados, None)

participantes_cargados = False
puntuajes_cargados = False

# M E N U
# 1. Cargar Nombres Participante
# 2. Cargar puntaje del jurado
# 3. Mostrar puntuaciones
# 4. Ver participantes con promedio menor a 4%
# 5. Ver participantes con promedio menor a 8%
# 6. Ver promedio de puntuaciones de cada jurado
# 7. Mostrar al Jurado más estricto
# 8. Mostrar al Jurado más generoso
# 9. Ver los Participantes con puntuaciones iguales
# 10. Buscar participante por nombre
# 11. Salir

mensaje_menu = "1.Cargar Nombres Participante\n2.Cargar puntaje del jurado\n3.Mostrar puntuaciones\n4.Ver participantes con promedio menor a 4%\n5.Ver participantes con promedio menor a 8%\n6.Ver promedio de puntuaciones de cada jurado\n7.Mostrar al Jurado más estricto\n8.Mostrar al Jurado más generoso\n9.Ver los Participantes con puntuaciones iguales\n10.Buscar participante por nombre\n11.Salir\n"
mensaje_error_carga = (
    "✖️  Debe cargar los participantes y las puntuaciones antes de ver los promedios."
)

while True:
    print(mensaje_menu)

    opcion = get_int("Selecciona una opcion: ", mensaje_menu, 1, 11)

    if opcion == 1:
        respuesta_registro = cargar_nombres_participantes(array_nombres)
        if respuesta_registro:
            os.system("cls")
            print("✔️  Se han regitrado los siguientes participantes:")
            mostrar_array(array_nombres)
            participantes_cargados = True
        else:
            print("Error al realizar la carga de nombres, intente nuevamente.\n")
    elif opcion == 2:
        respuesta_puntos = cargar_puntuaciones_jurado(matriz_puntuajes, array_nombres)
        if respuesta_puntos:
            print("✔️  Puntuajes cargados correctamente.")
            mostrar_matriz(matriz_puntuajes)
            puntuajes_cargados = True
        else:
            print("Error al realizar la carga de puntuaciones, intente nuevamente.\n")
    elif opcion == 3:
        if not mostrar_puntuaciones(matriz_puntuajes, array_nombres):
            print(mensaje_error_carga)
    elif opcion == 4:
        if not (participantes_cargados and puntuajes_cargados):
            print(mensaje_error_carga)
        else:
            if not mostrar_participantes_promedio_menor(
                matriz_puntuajes, array_nombres, 4
            ):
                print(mensaje_error_carga)
    elif opcion == 5:
        if not (participantes_cargados and puntuajes_cargados):
            print(mensaje_error_carga)
        else:
            if not mostrar_participantes_promedio_menor(
                matriz_puntuajes, array_nombres, 8
            ):
                print(mensaje_error_carga)
    elif opcion == 6:
        if not puntuajes_cargados:
            print(mensaje_error_carga)
        else:
            mostrar_promedio_por_jurado(matriz_puntuajes)
    elif opcion == 7:
        if not puntuajes_cargados:
            print(mensaje_error_carga)
        else:
            mostrar_jurados_mas_exigente(matriz_puntuajes)
    elif opcion == 8:
        if not puntuajes_cargados:
            print(mensaje_error_carga)
        else:
            mostrar_jurado_mas_generoso(matriz_puntuajes)
    elif opcion == 9:
        if not (participantes_cargados and puntuajes_cargados):
            print(mensaje_error_carga)
        else:
            encontrar_participantes_promedios_iguales(matriz_puntuajes, array_nombres)
    elif opcion == 10:
        if not (participantes_cargados and puntuajes_cargados):
            print(mensaje_error_carga)
        else:
            buscar_participantes(array_nombres, matriz_puntuajes)
    elif opcion == 11:
        print("Saliendo...")
        break
    input("Toque cualquier boton para continuar...")
    os.system("cls")
