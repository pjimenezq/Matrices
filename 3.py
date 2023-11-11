print("Este programa permite obtener la matriz transpuesta de una matriz ingresada.")#Propósito del programa

def transpuesta(A):#Función para obtener la matriz transpuesta
    C=[]#Se crea un arreglo vacio para la matriz C (que corresponde al resultado de la matriz transpuesta)
    filas=[]#Se crea un arreglo vacio que corresponde a las filas que se van a agregar a la matriz C
    for a in range(len(A[0])):#Para cada elemento a desde 0 hasta la cantidad de columnas de la matriz A
        for b in range(len(A)):#Para cada elemento b desde 0 hasta la cantidad de filas de la matriz A
            filas.append(A[b][a])#Agregar al arreglo vacio nombrado "filas" el elemento ubicado en la fila b, columna a
        C.append(filas)#Agregar los elementos del arreglo "filas" a la matriz C
        filas=[]#Se vacia el arreglo "filas"
    return C#La función retorna la matriz tranpuesta C

if __name__=="__main__":
    #El usuario ingresa la cantidad de filas, la cantidad de columnas y los elementos de la matriz A
    fils=[]
    A=[]
    nFilasA = int(input("Ingrese la cantidad de filas de la matriz: "))
    nColsA = int(input("Ingrese la cantidad de columnas de la matriz: "))
    for i in range(nFilasA):
        for j in range(nColsA):
            cFilas = int(input("Ingrese el número que se ubica en la columna "+ str(j)+ " y la fila " + str(i)+ ": "))
            fils.append(cFilas)#Se agregan los elementos de la fila a una lista que está vacia (esta lista se llama "fils")
        A.append(fils)#Se agrega la lista de los elementos de la fila a la matriz A
        fils = []# Se vacia la lista
    print("La matriz ingresada es: ")#Se imprime la matriz A
    for y in range(len(A)):
        print(A[y])

    matrizTranspuesta=transpuesta(A)#Se llama la función para obtener la transpuesta
    print("La matriz transpuesta es: ")
    for x in range(len(matrizTranspuesta)):
     print(matrizTranspuesta[x])#Se imprime el resultado de la matriz transpuesta