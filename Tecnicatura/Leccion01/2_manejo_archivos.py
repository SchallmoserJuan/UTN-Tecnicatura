# Declaracion de variable

# Crear un archivo
try:
    archivo = open('prueba.txt','w', encoding = 'utf8') # Si no existe lo va a crear       || w -> write = escribir
    archivo.write('Estamos escribiendo con .write en un archivo\n') # Escribir en el archivo

    # Modificacion o adicion
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('Segunda linea de modificación\n')

    archivo.write('Segunda linea de escritura')
except Exception as e:
    print(e)
finally: # Este siempre se ejecuta
    archivo.close() # Con esto se cierra el archivo
