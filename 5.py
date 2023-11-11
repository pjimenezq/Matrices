print("Este programa permite sumar los elementos de una fila dada de una matriz")#Propósito del programa

def sumaFila(A,fila):#Función para obtener la suma de los elementos de la fila de una matriz
    x:int=0#Se declara e inicializa x, como un entero con valor 0
    for i in range (len(A[0])):#Para cada elemento i desde 0 hasta la cantidad de columnas de la matriz A
        x+=A[fila][i]#Se suman todos los elementos ubicados en la fila dada por el usuario y la columna i
    return x#Se retorna el valor final de la suma de los elementos de la fila

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
        fils = []#Se vacia la lista
    print("La matriz ingresada es: ")#Se imprime la matriz
    for x in range(len(A)):
        print(A[x])

    fila=int(input("Ingrese el número de la fila, para sumar sus elementos: "))#El usuario ingresa el número de la fila de la que desea hallar la suma
    
    sumaElementosFila=sumaFila(A,fila)#Se llama a la función de suma de elementos de una fila
    print("La suma de los elementos de la fila " +str(fila)+ " es: "+ str(sumaElementosFila))#Se imprime el resultado de la suma