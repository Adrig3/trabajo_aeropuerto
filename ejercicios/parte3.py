reservas = [
    "Juan Pérez, Economy, Madrid",
    "14B, María López, Business, París",
    "21C, Economy, Madrid",
    "05D, Ana Sánchez, Londres",
    "19E, Luis Gómez, Economy, París",
    "08F, Sofía Vargas, Economy",
    25,
    None,
    True,
    " ",
    "51G, Paco Sans, Business, Dinamarca",
    "26G, María García, First, París",
    "70C, María García, CLASE EQUIVOCADA, París",

]

archivos_creados = {}
clases_reserva = ["Economy", "Business", "First"]

"""
Crea y escribe en el archivo de reservas 'reservas_maestro_con_errores.txt'.

Parámetros: ninguno.
Devuelve: None. En caso de error imprime un mensaje explicativo.
"""
def crear_y_escribir_archivo_maestro_errores():
    try:
        with open("reservas_maestro_con_errores.txt", "w", encoding="utf-8") as f:
            for reserva in reservas:
                try:
                    f.write(f"{reserva}\n")

                except (TypeError, ValueError) as err:
                    print(f"Error al escribir reserva {reserva}: {err}")

        print("Archivo 'reservas_maestro_con_errores.txt' creado con éxito.")

    except FileNotFoundError:
        print("Error: No se pudo encontrar la ruta para crear el archivo.")

    except PermissionError:
        print("Error: No tienes permiso para escribir en este directorio.")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")

"""
Recibe por parámetro una línea y sus datos ya separados.
Verifica que la línea sea válida según los criterios establecidos.

En caso de no ser válida, devuelve False y el tipo de error.
En caso de serlo, devuelve True y una cadena vacía.

Parámetros:
    - linea (str): la línea completa del archivo.
    - datos (list): los datos de la línea ya separados.

Devuelve (bool, str): Por un lado devuelve un booleano que indica si la línea es válida o no. 
                        Por otro lado devuelve una cadena con el tipo de error o vacía si no hay error.
"""
def linea_is_ok(linea, datos):
    if isinstance(linea, str) and linea.strip() == "":
        return False, "Línea vacía"
    
    if len(datos) < 4:
        return False, "Línea incompleta"
    
    if datos[2] not in clases_reserva:
        return False, "Clase de reserva inválida"
    
    if len(datos) == 4:
        return True, ""

    return False, "Error de formato"

"""
Lee el archivo reservas_maestro_con_errores.txt, 
Separa la linea en campos y llama a la función linea_is_ok para verificar si la línea es válida.

Si la línea es válida, la escribe en un archivo correspondiente al destino.
Si no lo es, se registra en registro_errores.log (se crea si no existe) 
con los detalles del error y no se incorpora a los demás.

El formato de registro_errores.log es:
[Fecha y hora] Línea: <contenido de la línea> - Error: <descripción del error>

Parámetros: ninguno.
Devuelve: El numero de archivos creados. En caso de error imprime un mensaje explicativo.
"""
def verificar_reservas():
    try:
        with open("reservas_maestro_con_errores.txt", "r", encoding="utf-8") as f:
            for linea in f:
                datos = linea.strip().split(", ")
                linea_ok, tipoError = linea_is_ok(linea, datos)

                if linea_ok:
                    asiento, nombre, clase, destino = datos
                    nombre_archivo = f"reservas_{destino.lower()}.txt"

                    try:
                        with open(nombre_archivo, "a", encoding="utf-8") as archivo_destino:
                            archivo_destino.write(linea)

                        if nombre_archivo not in archivos_creados:
                            archivos_creados[nombre_archivo] = 0

                        archivos_creados[nombre_archivo] += 1

                    except FileNotFoundError:
                        return f"Error: No se encontró el archivo '{nombre_archivo}'."

                    except PermissionError:
                        return f"Error: No tienes permiso para escribir en '{nombre_archivo}'."

                    except Exception as e:
                        return f"Ha ocurrido un error inesperado con '{nombre_archivo}': {e}"

                else:
                    try:
                        with open("registro_errores.log", "a", encoding="utf-8") as log_errores:
                            from datetime import datetime
                            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            log_errores.write(f"[{fecha_hora}] Línea: {linea.strip()} - Error: {tipoError}\n")

                    except FileNotFoundError:
                        return f"Error: No se encontró el archivo '{log_errores}'."

                    except PermissionError:
                        return f"Error: No tienes permiso para escribir en '{log_errores}'."

                    except Exception as e:
                        return f"Ha ocurrido un error inesperado con '{log_errores}': {e}"

    except FileNotFoundError:
        return "Error: No se encontró el archivo 'reservas_maestro_con_errores.txt'."

    except PermissionError:
        return "Error: No tienes permiso para leer el archivo 'reservas_maestro_con_errores.txt'."

    except Exception as e:
        return f"Ha ocurrido un error inesperado: {e}"
    
    return f"Se han creado {sum(archivos_creados.values())} reservas con formato correcto en total."

"""
Muestra por terminal un resumen de los archivos creados y la cantidad de reservas en cada uno.

Parámetros: numero de archivos creados.
Devuelve: None.
"""

def mostrar_resumen_archivos():
    if not archivos_creados:
        print("No se han creado archivos de reservas por destino.")
        return

    try:
        print("\nResumen de la clasificación:")
        for archivo, cantidad in archivos_creados.items():
            print(f"- {archivo}: {cantidad} reservas")

        print("-"*30)
        print("Imprimiendo los errores...")
        with open("registro_errores.log", "r", encoding="utf-8") as log_errores:
            for linea in log_errores:
                print(linea.strip())

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{log_errores}'.")

    except PermissionError:
        print(f"Error: No tienes permiso para leer el archivo '{log_errores}'.")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado al mostrar el resumen de archivos: {e}")