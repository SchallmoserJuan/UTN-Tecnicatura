# Para leer un archivo tenemos varios modos
# uno de ellos (que viene por default) es el 'r' de read

archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())

#Copiar archivo a otro
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()
archivo2.close()

print('Fin del proceso')