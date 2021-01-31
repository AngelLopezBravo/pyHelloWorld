import shutil

origen = r'c:\temp\origen.txt'
destino = r'c:\temp\destino.txt'
shutil.copyfile(origen,destino)


Vertical  = input('Indique Vertical: ')
Equipo = input('Indique Nombre del Equipo: ')

archivo = open(destino, "r")
datos = archivo.read()
print('datos; ', datos)

datos = datos.replace('<Vertical>', Vertical)
datos = datos.replace('<Nombre del equipo>', Equipo)

archivo = open(destino, "w")
archivo.write(datos)
archivo.close()

archivo = open(destino, "r")
print('datos; ', archivo.read())

