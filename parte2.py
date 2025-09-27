"""
Datos de reservas, formato: Asiento, Nombre, Clase, Destino
"""
reservas = [
    "12A, Juan Pérez, Economy, Madrid",
    "14B, María López, Business, París",
    "21C, Carlos García, Economy, Madrid",
    "05D, Ana Sánchez, Business, Londres",
    "19E, Luis Gómez, Economy, París",
    "08F, Sofía Vargas, Economy, Londres"
]

"""
Crea y escribe en el archivo de reservas 'reservas_maestro.txt'.
"""
try:
    with open("reservas_maestro.txt", "w", encoding="utf-8") as f:
        for reserva in reservas:
            f.write(reserva + "\n")

    print("Archivo 'reservas_maestro.txt' creado con éxito.")

except FileNotFoundError:
    print("Error: No se pudo encontrar la ruta para crear el archivo.")

except PermissionError:
    print("Error: No tienes permiso para escribir en este directorio.")

except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")


"""
Lee el archivo reservas_maestro.txt, identifica el destino del
vuelo y crear archivos por destino (sin duplicados).

Si hay una linea de reservas incompleta, esa linea en concreto,
no se añadirá a ningún archivo.


Cuenta cuántas reservas hay en cada archivo creado, lo guarda en
la variable 'archivos_creados' para luego mostrarlos por terminal.
"""
archivos_creados = {}

try:
    with open("reservas_maestro.txt", "r", encoding="utf-8") as f:
        for linea in f:
            datos = linea.strip().split(", ")
            if len(datos) == 4:
                asiento, nombre, clase, destino = datos
                nombre_archivo = f"reservas_{destino.lower()}.txt"

                try:
                    with open(nombre_archivo, "a", encoding="utf-8") as archivo_destino:
                        archivo_destino.write(linea)

                    if nombre_archivo not in archivos_creados:
                        archivos_creados[nombre_archivo] = 0
                    archivos_creados[nombre_archivo] += 1

                except FileNotFoundError:
                    print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
                except PermissionError:
                    print(f"Error: No tienes permiso para escribir en '{nombre_archivo}'.")
                except Exception as e:
                    print(f"Ha ocurrido un error inesperado al escribir en '{nombre_archivo}': {e}")
            else:
                print(f"Línea incompleta: {linea}, no se ha sido añadida a ningún archivo.")

except FileNotFoundError:
    print("Error: No se encontró el archivo 'reservas_maestro.txt'.")

except PermissionError:
    print("Error: No tienes permiso para leer el archivo 'reservas_maestro.txt'.")

except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")

"""
Verificación y conteo final
"""
print("\nResumen de la clasificación:")
for archivo, cantidad in archivos_creados.items():
    print(f"- {archivo}: {cantidad} reservas")
