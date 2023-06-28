listaRUTdest = []
listaNombre = []
listaTipo = []
listaDestinatario= []
listaPeso= []
listaPrecio=[]
ciudadDest=[]
listaEncomiendas=[]

menu='''
1.Grabar
2.Buscar
3.Lista de encomiendas
4.Salir
'''
def grabar():
    while True:
        try:
            rut = input('Inserte el rut: ')
            if len(rut)>=9 and rut.count('-')== 1(len(rut.split('-')[0])==9)and (1<=len(rut.split('-')[1])):
                listaRUTdest.append(rut)
                print('ingrese un rut correcto')
                break
            else:
                print('ingreso un rut correcto')
        except:
            print('Excepcion en RUT')

while True:
    try:
        nombre= input('Ingrese el nombre: ')
        if len(nombre)<= 3:
            print('ingrese un nombre valido')
        else:
            listaNombre.append(nombre)
            print('ingreso de nombre correcto')
            break
    except:
        print('excepcion en nombre')
while True:
    try:
        tipo = input('Ingrese el tipo de paquete: ')
        if len(tipo)<= 3:
            print('ingrese un tipo valido')
        else:
            listaTipo.append(tipo)
            print('ingreso de tipo correcto')
            break
    except:
        print('excepcion en nombre')
while True:
    try:
        peso= input('Ingrese el peso: ')
        if float(peso)<= 0.1:
            print('ingrese un peso valido')
        else:
            listaPeso.append(peso)
            print('ingreso de peso correcto')
            break
    except:
        print('excepcion en nombre')

while True:
    try:
        precio= input('Ingrese el peso: ')
        if int(precio)<= 2000:
            print('ingrese un peso valido')
        else:
            listaPrecio.append(precio)
            print('ingreso de peso correcto')
            break
    except:
        print('excepcion en nombre')

def buscar():
    while True:
        try:
            buscar = input('ingrese el rut para buscar: ')
            if buscar in listaRUTdest.index(buscar):
            index= listaRUTdest.index(buscar)
            print('|N | NOMBRE     | RUT        | PESO       | PRECIO       |')
            print('|  +------------+------------+------------+--------------|')
            for i in range (len(listaRUTdest)):
                print(f'|{i:2d}|{listaNombre[index]:20s}|{listaRUTdest[index]:15s}|{listaPeso[index]:5d}|{listaPrecio[index]:7d}')
                print('|  +------------+------------+------------+--------------|')
                break
            else:
                print('No se encuentra Encomienda en el sistema')
        except:
            print('excepcion en buscar')

def listadeEncomiendas():
    while True:
        try:
            lista = int(input(listadeEncomiendas))
            if lista in listaEncomiendas.index(lista):
            index = listaEncomiendas.index(lista)
            print('|N | NOMBRE     | RUT        | PESO       | PRECIO       |')
            print('|  +------------+------------+------------+--------------|')
            for i in range (len(listaRUTdest)):
                print(f'|{i:2d}|{listaNombre[index]:20s}|{listaRUTdest[index]:15s}|{listaPeso[index]:5d}|{listaPrecio[index]:7d}')
                print('|  +------------+------------+------------+--------------|')
                break
            else:
                print('No se encuentra Encomienda en el sistema')
        except:
            print('excepcion en buscar')
def menu():
    while True:
        try: opcion = int(input(menu))
            if opcion == 1:
                grabar()
            elif opcion == 2:
                buscar()
            elif opcion == 3:
                listadeEncomiendas()
            elif opcion == 4:
                break
            else:
                print('Ingrese una opcion valida')
    except:
        print('excepcion en menu')




