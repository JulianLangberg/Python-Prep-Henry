import sys
# 1) Crear un script con el nombre "clase09_ej1.py" que reciba 3 parametros a elección,
#  verificando que sean exactamente esa cantidad,y muestre como salida los parámetros recibidos

if len(sys.argv) == 4:
    print("El primer parámetro es:",sys.argv[1])
    print("El segundo parámetro es:",sys.argv[2])
    print("El tercer parámetro es:",sys.argv[3])
else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print('Ejemplo: clase09_ej1.py 1 2 3')
