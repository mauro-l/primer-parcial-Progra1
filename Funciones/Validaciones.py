def validar_entero(cadena: str) -> bool:
    """
    Verifica si la cadena recibida representa un número entero positivo.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si la cadena es un entero positivo, False en caso contrario.
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            valor_ascii = ord(cadena[i])
            if valor_ascii > 57 or valor_ascii < 48:
                retorno = False
                break
    else:
        retorno = False

    return retorno


def validar_string(texto: str) -> bool:
    """
    Valida que el texto recibido contenga solo letras y espacios.
    Args:
        texto (str): Cadena a validar.
    Returns:
        bool: True si es válido (solo letras y espacios y no vacío), False si no.
    """
    if len(texto) > 0:
        for i in range(len(texto)):
            valor_ascii = ord(texto[i])
            if not (
                (valor_ascii >= 65 and valor_ascii <= 90)  # A-Z
                or (valor_ascii >= 97 and valor_ascii <= 122)  # a-z
                or valor_ascii == 32
            ):
                print(
                    f"Error: El carácter '{texto[i]}' no está permitido. Solo letras y espacios\n"
                )
                return False
        return True
    else:
        print("Error: El texto no puede estar vacío.")
        return False


def validar_array(array: list) -> bool:
    """
    Valida que el array no sea nulo y tenga al menos un elemento.

    Args:
        array (list): Array a validar.

    Returns:
        bool: True si es válido, False si es nulo o vacío.
    """
    if type(array) == list and len(array) > 0:
        return True
    else:
        return False
