import sympy as sy
import numpy as np

###############################Ejemplos#######################################
#matrix=([[2,1,-1,-6,3],[3,0,2,1,-5],[4,1,2,-2,-1],[2,8,-8,5,-7]])#Unica
#m=4;n=5
#matrix=([[-1,2,5,2],[3,1,8,7],[2,1,3,12],[0,0,0,0],[0,0,0,0]])#Unica
#m=5;n=4
#matrix=([[-1,2,5],[3,1,7],[0,0,0],[0,0,0],[0,0,0]])#sin solucion
#m=5;n=3
#matrix=([[2,1,-1,-6],[3,-1,1,-5],[4,2,-2,-1]])#Sin solucion
#m=3;n=4
matrix=([[1,3,1,1,5,8,9],[0,0,0,0,0,0,0],[0,0,8,0,0,0,0],[0,0,0,0,0,7,0]])#Infinitas
m=4;n=7
#matrix=([[2,4,6,18],[4,5,6,24],[2,7,12,30]])#Infinitas
#m=3;n=4

#Para llenar la matrix de forma manual
'''m=int(input('cantidad de filas:')) #filas
n=int(input('cantidad de columnas:')) #columnas
matrix = np.zeros((m,n)) 
print ('Ingrese la matriz de coeficientes')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))
'''
M = sy.Matrix(matrix)
t =np.array(M.rref()[0])
print(t)
d=0
unos = []
e=0
#Ciclo para ver si la matriz tiene solucion infinita o no tiene solucion
for i in range(0,m):
    e = 0
    for j in range(0,n-1):
        if (t[i][j] == 1 and e == 0):
            unos.append([i,j])
            e=1
#print(unos)    
no = 0
if(len(unos) != m):
    for i in range(len(unos),m):
        if(t[i][n-2]==0 and t[i][n-1]!=0):
            print("No tiene solucion")
            no = 1
if(no == 0):
    zero = 0
    for i in range(unos[len(unos)-1][0]+1,m):
            for j in range(0,n):
                if(t[i][j]!=0):
                    zero = 1
                    break
    if(n-m>=2):
        print("Tiene infinitas soluciones")
    else:
        if(zero == 0):
            if (len(unos) == n-1):
                print("Tiene unica solucion")
            else:
                print("Tiene infinitas soluciones")
        else:
            print("Tiene unica solucion")
    
