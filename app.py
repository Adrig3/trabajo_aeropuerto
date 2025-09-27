import parte1
import parte2
import parte3
import time

print("--- INICIO EJERCICIO 1 ---")
time.sleep(1)
print("1.- Se va a crear el fichero de reservas.")
time.sleep(1)
parte1.crear_archivo_reservas()
print("- Se ha creado el fichero reservas.txt")
time.sleep(1)
print(" ")

print("2.- Se van a escribir las reservas en el fichero.")
time.sleep(1)
parte1.escribir_archivo_reservas()
print("- Se han escrito las reservas en el fichero reservas.txt")
time.sleep(1)
print(" ")

print("3.- Se van a leer las reservas del fichero.")
time.sleep(1)
parte1.leer_reservas()
time.sleep(1)
print(" ")

print("4.- Se van a contar las reservas del fichero.")
time.sleep(1)
print(parte1.contar_reservas())
time.sleep(1)
print(" ")

print("5.- Se van a filtrar las reservas por la clase 'Business'.")
time.sleep(1)
parte1.filtrar_reservas_por_clase("Business")
time.sleep(1)
print("--- FIN EJERCICIO 1 ---")
print(" ")

print("--- INICIO EJERCICIO 2 ---")
time.sleep(1)
print("1.- Se ha creado el fichero reservas_maestro.txt con las reservas.")
parte2.crear_y_escribir_archivo_maestro()
time.sleep(1)
print(" ")

print("2.- Se van a clasificar las reservas por destino.")
archivos_creados = parte2.clasificar_reservas_por_destino()
print("Se han clasificado un total de: " + str(sum(archivos_creados.values())) + " archivos.")
time.sleep(1)
print(" ")

print("3.- Se va a mostrar un resumen de los archivos creados.")
parte2.mostrar_resumen_archivos(archivos_creados)
time.sleep(1)
print("--- FIN EJERCICIO 2 ---")

print("--- INICIO EJERCICIO 3 ---")
time.sleep(1)
print("1.- Se ha creado el fichero reservas_maestro_con_errores.txt con las reservas.")
parte3.crear_y_escribir_archivo_maestro_errores()
time.sleep(1)
print(" ")

print("2.- Se van a verificar las reservas y clasificar por destino.")
archivos_creados_errores = parte3.verificar_reservas()
print(archivos_creados_errores)
time.sleep(1)
print(" ")

print("3.- Se va a mostrar un resumen de los archivos creados.")
parte3.mostrar_resumen_archivos()
time.sleep(1)
print("--- FIN EJERCICIO 3 ---")