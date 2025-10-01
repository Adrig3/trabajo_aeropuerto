# 📌 Gestión de Reservas de Vuelos


## 🚀 Ejecución del programa

El código principal que se debe ejecutar es **`app.py`**.  
Este archivo contiene la ejecución de los tres apartados del ejercicio, por sus respectivos métodos:

1. **Ejercicio 1** (archivo `parte1.py`):  
   - Creación de un fichero inicial de reservas (`reservas.txt`).  
   - Escritura de las reservas en el fichero.  
   - Lectura de las reservas desde el fichero.  
   - Conteo del número de reservas.  
   - Filtrado de reservas por clase (ejemplo: *Business*).

2. **Ejercicio 2** (archivo `parte2.py`):  
   - Creación del fichero maestro de reservas (`reservas_maestro.txt`).  
   - Clasificación de reservas en diferentes archivos según el destino.  
   - Resumen de los archivos creados, mostrando el número de reservas en cada uno.  

3. **Ejercicio 3** (archivo `parte3.py`):  
   - Creación de un fichero maestro con reservas erróneas (`reservas_maestro_con_errores.txt`).  
   - Verificación y validación de reservas (detectando errores de formato o datos inválidos).  
   - Clasificación de las reservas correctas por destino.  
   - Registro de los errores en un archivo de log (`registro_errores.log`).  
   - Resumen final con listado de reservas válidas y errores detectados.  



## 📚 Documentación
Se ha implementado una **clase `Reserva`** en los módulos `parte1.py` y `parte2.py` para estructurar los datos de cada reserva (asiento, nombre, clase, destino).  

Cada función y clase está documentada con **docstrings** en formato claro, donde se especifican:  
- **Parámetros** que recibe.  
- **Valor de retorno** esperado.  
- **Manejo de errores** en casos de excepciones comunes (ficheros no encontrados, permisos, líneas mal formadas, etc.).  



## ⚠️ Problemas encontrados

- **Problema:** Al escribir en los ficheros, los caracteres con tilde o la `ñ` aparecían mal formados.  
- **Causa:** No se estaba especificando el formato de codificación al abrir los archivos.  
- **Solución:** Añadir `encoding="utf-8"` en cada sentencia `with open`.  
- **Prompts planteado a ChatGPT:**  
<br>

  - *"Tengo un problema enviando texto a un fichero en python, no se como formatear el texto a utf8 en el with open. Explica breve y detalla lo que has añadido."*  

```python
with open("reservas.txt", "w", encoding="utf-8") as archivo:
    ...
```
---



### ✍️ Creado por:  
**Adrià Garí, Gabriel Santandreu y Daniel Cobo**
