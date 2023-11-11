print("Este programa permite sumar los elementos de una columna dada de una matriz")#Propósito del programa

def sumaColumna(A,columna):#Función para obtener la suma de los elementos de la columna de una matriz
    x:int=0#Se declara e inicializa x, como un entero con valor 0
    for i in range (len(A)):#Para cada elemento i desde 0 hasta la cantidad de filas de la matriz A
        x+=A[i][columna]#Se suman todos los elementos ubicados en la fila i y la columna dada por el usuario
    return x#Se retorna el valor final de la suma de los elementos de la columna

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

    columna=int(input("Ingrese el número de la columna, para sumar sus elementos: "))#El usuario ingresa el número de la columna de la que desea hallar la suma

    sumaElementosColumna=sumaColumna(A,columna)#Se llama a la función de suma de elementos de una columna
    print("La suma de los elementos de la columna " +str(columna)+ " es: "+ str(sumaElementosColumna))#Se imprime el resultado de la suma