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
print("Este programa permite calcular el producto de matrices.")#Propósito del programa
print("Recuerde que para poder multiplicar dos matrices es necesario que el número de columnas de la primera matriz sea igual al número de filas de la segunda matriz.")#Estableciendo las condiciones del programa

def multiplicacion(A,B):#Función para calcular el producto de matrices
    C=[]#Se crea un arreglo vacio para la matriz C (que corresponde al resultado de la multiplicación de las dos matrices)
    fila=[]#Se crea un arreglo vacio que corresponde a las filas que se van a agregar a la matriz C
    elemento=[]#Se crea un arreglo vacio que corresponde a aquellos elementos que se van a sumar para ser agregados al arreglo llamado fila, y luego a la matriz C
    y:int=0#Se declara e inicializa la variable y, que tiene un valor de 0
    for i in range (len(A)):#Para cada elemento i desde 0 hasta la cantidad de filas de la matriz A
        for j in range(len(B[0])):#Para cada elemento j desde 0 hasta la cantidad de columnas de la matriz B
            for k in range(len(A[0])):#Para cada elemento k desde 0 hasta la cantidad de columna de la matriz A
                elemento.append(A[i][k]*B[k][j])#Se agrega al arreglo vacio nombrado "elemento" la multiplicación del elemento ubicado en la fila i, columna k de la matriz A por el elemento ubicado en la fila k, columna j de la matriz B
            for x in elemento:#Para cada elemento en el arreglo "elemento"
                y+=x#Se calcula la sumatoria de los elementos del arreglo
            fila.append(y)#Se agraga la sumatoria al arreglo llamado "fila"
            elemento=[]#Se vacia el arreglo "elemento"
            y=0#Se inicializa y en 0
        C.append(fila)#Se agrega el elemento del arreglo "fila" a la matriz C
        fila=[]#Se vacial el arreglo "fila"
    return C#Al finalizar las operaciones para hallar el producto de matrices, la función retorna la matriz C
    
if __name__=="__main__":
    #El usuario ingresa la cantidad de filas, la cantidad de columnas y los elementos de la matriz A
    fils=[]
    A=[]
    nFilasA = int(input("Ingrese la cantidad de filas de la primera matriz: "))
    nColsA = int(input("Ingrese la cantidad de columnas de la primera matriz: "))
    for i in range(nFilasA):
        for j in range(nColsA):
            cFilas = int(input("Ingrese el número que se ubica en la columna "+ str(j)+ " y la fila " + str(i)+ ": "))
            fils.append(cFilas)#Se agregan los elementos de la fila a una lista que está vacia (esta lista se llama "fils")
        A.append(fils)#Se agrega la lista de los elementos de la fila a la matriz A
        fils = []#Se vacia la lista
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
        fils = [] #Se vacia la lista
    print("La segunda matriz ingresada es: ")#Se imprime la segunda matriz
    for y in range(len(B)):
        print(B[y])

    if nColsA!=nFilasB:#Cuando no se cumplen las condiciones (el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz), no se puede realizar la operación de multiplicación
        print("Las matrices no cumplen las condiciones necesarias para ejecutar la operación")
        print("Recuerde que el número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz para poder multiplicar las dos matrices")
    else:##En caso de que las matrices ingresadas si cumplan las condiciones
        producto=multiplicacion(A,B)#Se llama la función de multiplicación
        print("El producto de las matrices es: ")
        for i in range (len(producto)):
            print(producto[i])#Se imprime el resultado de la multiplicación de matrices
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
