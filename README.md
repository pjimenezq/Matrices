# Reto 11: Matrices

**Instrucciones**

Para cada punto cree un programa individual. Al finalizar suba todo a un repo y súbalo al canal reto_11 en slack. Todos los puntos deben estar debidamente comentados y utilizar funciones para su desarrollo.
## Punto uno
Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

**Código**
```
print("Este programa permite sumar y restar matrices")#Propósito del programa
print("Recuerde que dos matrices tienen que tener un número igual de filas y columnas para poder sumarlas o restarlas")#Estableciendo las condiciones del programa

def suma(A,B):#Función para calcular la suma de matrices
    for i in range(len(B)): # Recorre filas de la matriz
        for j in range(len(B[i])): # Recorre cada elemento de la fila
            A[i][j] = A[i][j]+B[i][j]#Suma los dos elementos que se encuentran en la misma columna y la misma fila de ambas matrices
    return (A)#La función retorna la matriz A, tras haber sumado las dos matrices

def resta(A,B):#Función para calcular la resta de matrices
    for i in range(len(B)): # Recorre filas de la matriz
        for j in range(len(B[i])): # Recorre cada elemento de la fila
            A[i][j] = A[i][j]-B[i][j]#Resta los dos elementos que se encuentran en la misma columna y la misma fila de ambas matrices
    return (A)#La función retorna la matriz A, tras haber restado las dos matrices
    
if __name__=="__main__":
    
    sumaOResta=str(input("Ingrese la palabra SUMA o la palabra RESTA según la operación que quiera realizar: "))#El usuario decide si quiere realizar una suma o una resta

    #El usuario ingresa la cantidad de filas, la cantidad de columnas y los elementos de la matriz A
    filas=[]
    A=[]
    nFilasA = int(input("Ingrese la cantidad de filas de la primera matriz: "))
    nColsA = int(input("Ingrese la cantidad de columnas de la primera matriz: "))
    for i in range(nFilasA):
        for j in range(nColsA):
            cFilas = int(input("Ingrese el número que se ubica en la columna "+ str(j)+ " y la fila " + str(i)+ ": "))
            filas.append(cFilas)#Se agregan los elementos de la fila a una lista que está vacia (esta lista se llama "filas")
        A.append(filas)#Se agrega la lista de los elementos de la fila a la matriz A
        filas = []#Se vacia la lista
    print("La primera matriz ingresada es: ")#Se imprime la primera matriz
    for x in range(len(A)):
        print(A[x])
    
    #El usuario ingresa la cantidad de filas, la cantidad de columnas y los elementos de la matriz B
    fils=[]
    B=[]
    nFilasB = int(input("Ingrese la cantidad de filas de la segunda matriz: "))
    nColsB = int(input("Ingrese la cantidad de columnas de la segunda matriz: "))
    for i in range(nFilasB):
        for j in range(nColsB):
            cFilas = int(input("Ingrese el número que se ubica en la columna "+ str(j)+ " y la fila " + str(i)+": "))
            fils.append(cFilas)#Se agregan los elementos de la fila a una lista que está vacia (esta lista se llama "fils")
        B.append(fils)#Se agrega la lista de los elementos de la fila a la matriz B
        fils = []  #Se vacia la lista
    print("La segunda matriz ingresada es: ")#Se imprime la segunda matriz
    for y in range(len(B)):
        print(B[y])

    if nFilasA!=nFilasB or nColsA!=nColsB:#Cuando no se cumplen las condiciones (las dos matrices tienen que tener un número igual de filas y columnas), no se puede realizar las operaciones de suma y resta
        print("Las matrices no cumplen las condiciones necesarias para ejecutar la operación")
        print("Recuerde que dos matrices deben tener un número igual de filas y columnas para poder sumarlas o restarlas")

    else:#En caso de que las matrices ingresadas si cumplan las condiciones
        
        if sumaOResta=="SUMA":#Si el usuario ingresó "SUMA"
            sumaMatrices=suma(A,B)#Se llama la función de suma
            print("La suma de las matrices es: ")
            for z in range(len(sumaMatrices)):
                print(sumaMatrices[z])#Se imprime el resultado de la operación de la suma de matrices

        elif sumaOResta=="RESTA":#Si el usuario ingresó "RESTA"
            restaMatrices=resta(A,B)#Se llama la función de resta
            print("La resta de las matrices es: ")
            for z in range(len(restaMatrices)):
                print(restaMatrices[z])#Se imprime el resultado de la operación de la resta de matrices
```
## Punto dos
Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.

**Código**
```
```
## Punto tres
Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

**Código**
```
```
## Punto cuatro
Desarrollar un programa que sume los elementos de una columna dada de una matriz.

**Código**
```
```
## Punto cinco
Desarrollar un programa que sume los elementos de una fila dada de una matriz.

**Código**
```
```
