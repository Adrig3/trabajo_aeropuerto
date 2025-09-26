class Reserva:
    """Representa una reserva de asiento.

    Parámetros:
    - asiento (int): número de asiento.
    - nombre (str): nombre del pasajero.
    - clase (str): clase de la reserva (por ejemplo 'Economy', 'Business').

    Devuelve:
    - instancia de `Reserva`.
    """
    def __init__(self, asiento, nombre, clase):
        self.asiento = asiento
        self.nombre = nombre
        self.clase = clase


reservas = [
    Reserva(1, "Juan Perez", "Economy"),
    Reserva(2, "Maria Lopez", "Business"),
    Reserva(3, "Carlos Garcia", "Economy")
]


def crear_archivo_reservas():
    """Crea (o trunca) el fichero 'reservas.txt'.

    Parámetros: ninguno.
    Devuelve: None. En caso de error imprime un mensaje explicativo.
    """
    try:
        with open("reservas.txt", "w") as archivo:
            pass
    except PermissionError:
        print("Error: no tiene permisos para crear 'reservas.txt'.")
    except OSError as err:
        print(f"Error de sistema al crear 'reservas.txt': {err}")

def escribir_archivo_reservas():
    """Añade las reservas definidas en la lista global `reservas` al fichero.

    Parámetros: ninguno (usa la lista global `reservas`).
    Devuelve: None. En caso de error imprime un mensaje explicativo.
    """
    try:
        with open("reservas.txt", "a") as archivo:
            for reserva in reservas:
                try:
                    archivo.write(f"{reserva.asiento}, {reserva.nombre}, {reserva.clase}\n")
                except (TypeError, ValueError) as err:
                    print(f"Error al escribir reserva {reserva}: {err}")
    except FileNotFoundError:
        print("Error: archivo 'reservas.txt' no encontrado al intentar escribir.")
    except PermissionError:
        print("Error: no tiene permisos para escribir en 'reservas.txt'.")
    except OSError as err:
        print(f"Error de sistema al escribir en 'reservas.txt': {err}")

def leer_reservas():
    """Lee las reservas desde 'reservas.txt' y las muestra por pantalla.

    Parámetros: ninguno.
    Devuelve: None. En caso de líneas mal formadas las ignora e imprime un aviso; en caso de error de E/S imprime un mensaje.
    """
    try:
        with open("reservas.txt", "r") as archivo:
            for linea in archivo:
                try:
                    asiento, nombre, clase = linea.strip().split(",")
                except ValueError:
                    print(f"Aviso: línea mal formada en 'reservas.txt': {linea.strip()}")
                    continue
                print(f"Asiento: {asiento.strip()} | Nombre: {nombre.strip()} | Clase: {clase.strip()}")
    except FileNotFoundError:
        print("Error: 'reservas.txt' no existe. Cree el archivo primero.")
    except PermissionError:
        print("Error: no tiene permisos para leer 'reservas.txt'.")
    except OSError as err:
        print(f"Error de sistema al leer 'reservas.txt': {err}")


def contar_reservas():
    """Cuenta las reservas en 'reservas.txt'.

    Parámetros: ninguno.
    Devuelve: int con el número de reservas. Si no puede leer el archivo devuelve 0 e imprime un mensaje.
    """
    try:
        with open("reservas.txt", "r") as archivo:
            return sum(1 for linea in archivo)
    except FileNotFoundError:
        print("Error: 'reservas.txt' no existe. Devuelvo 0.")
        return 0
    except PermissionError:
        print("Error: no tiene permisos para leer 'reservas.txt'. Devuelvo 0.")
        return 0
    except OSError as err:
        print(f"Error de sistema al contar reservas en 'reservas.txt': {err}")
        return 0
    
def filtrar_reservas_por_clase(clase):
    """Muestra las reservas cuya clase coincide con el parámetro `clase`.

    Parámetros:
    - clase (str): nombre de la clase a filtrar (ej. 'Economy').

    Devuelve: None. Imprime las reservas coincidentes. En caso de línea mal formada la ignora; en caso de error de E/S imprime un mensaje.
    """
    try:
        with open("reservas.txt", "r") as archivo:
            for linea in archivo:
                try:
                    asiento, nombre, clase_reserva = linea.strip().split(",")
                except ValueError:
                    print(f"Aviso: línea mal formada en 'reservas.txt': {linea.strip()}")
                    continue
                if clase_reserva.strip() == clase:
                    print(f"Asiento: {asiento.strip()} | Nombre: {nombre.strip()} | Clase: {clase_reserva.strip()}")
    except FileNotFoundError:
        print("Error: 'reservas.txt' no existe. No hay reservas que filtrar.")
    except PermissionError:
        print("Error: no tiene permisos para leer 'reservas.txt'.")
    except OSError as err:
        print(f"Error de sistema al filtrar 'reservas.txt': {err}")