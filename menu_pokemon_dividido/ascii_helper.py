import os


def leer_ascii(ruta):
    """
    Lee el contenido de un archivo de texto ASCII y lo retorna.
    Se asume que la ruta es relativa a la carpeta 'ascii'
    """
    path_completo = os.path.join("ascii", ruta)
    try:
        with open(path_completo, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"Error al leer {ruta}: {e}"
