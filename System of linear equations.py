import sympy as sy
import numpy as np
#matrix=([[4,-3,1,8,3],[2,5,3,-1,2]])#Para infinitas soluciones
#m=2;n=5
#matrix=([[1,0,3,4,3,4],[0,1,3,-1,2,3],[0,0,1,-1,2,6]])#Para infinitas soluciones
#m=3;n=6
#matrix=([[2,1,-1,-6],[3,0,1,-5],[4,2,-2,-1],[2,8,5,-7]])#sin solucion
#m=4;n=4
#matrix=([[2,1,-1,-6,3],[3,0,2,1,-5],[4,1,2,-2,-1],[2,8,-8,5,-7]])#con solucion
#m=4;n=5
#matrix=([[1,1,0,0,200],[0,0,1,1,350],[1,0,1,0,300],[0,1,0,1,250]])#infinitas soluciones
#m=4;n=5
#matrix=([[1,1,2],[2,1,3],[4,1,2]])#Sin solucion
#m=3;n=3
#matrix=([[-1,2,5,2],[3,1,8,7],[2,1,3,12],[0,0,0,0],[0,0,0,0]])#Con solucion
#m=5;n=4
matrix=([[-1,2,5],[3,1,7],[0,0,0],[0,0,0],[0,0,0]])#sin solucion
m=5;n=3
#matrix=([[-1,2,5],[3,1,7],[2,3,12],[2,3,12],[2,3,12]])#Con solucion
#m=5;n=3
#matrix=([[-1,2,5,2,8],[3,1,5,7,7],[0,5,8,1,2],[0,0,0,0,1]])#En esta tira lo que no es
#m=4;n=5
#matrix=([[50,160,150,3030],[300,100,40,2700],[50,100,90,1950]])#infinitas soluciones  y 0=0
#m=3;n=4
#matrix=([[1,0,3,-2],[0,1,2,1],[0,0,0,0]])#infinitas soluciones  y 0=0
#m=3;n=4
#matrix=([[2,1,-1,-6],[3,-1,1,-5],[4,2,-2,-1]])#Sin solucion
#m=3;n=4
#matrix=([[1,-3,1,1],[1,-3,3,0],[2,-6,4,1]])#Infinitas
#m=3;n=4
#matrix=([[1,-3,1,1],[0,0,0,0],[0,0,0,0]])#infinitas
#m=3;n=4
#matrix=([[1,3,1,1,5,8,9],[0,0,0,0,1,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,1]])#Sin solucion
#m=4;n=7
#matrix=([[2,4,6,18],[4,5,6,24],[2,7,12,30]])#infinitas
#m=3;n=4

#Para llenar la matrix de forma manual
'''matrix=([[2,-3,1],[1,5,4],[3,4,2]])#Sin solucion
m=3;n=3
m=int(input('cantidad de filas:')) #filas
n=int(input('cantidad de columnas:')) #columnas
matrix = np.zeros((m,n)) 
q

print ('Ingrese la matriz de coeficientes')
for r in range(0,m):
    for c in range(0,n):
        matrix[(r),(c)]=float(input("Elemento a["+str(r+1)+str(c+1)+"] "))'''

M = sy.Matrix(matrix)
t =np.array(M.rref()[0])
print(t)
d=0
unos = [];
e=0;
#Ciclo para ver si la matriz tiene solucion infinita o no tiene solucion
for i in range(0,m):
    e = 0;
    for j in range(0,n-1):
        if (t[i][j] == 1 and e == 0):
            unos.append([i,j])
            e=1
print(unos)    
no = 0;
if(len(unos) != m):
    for i in range(len(unos),m):
        if(t[i][n-2]==0 and t[i][n-1]!=0):
            print("No tiene solucion")
            no = 1;
if(no == 0):
    zero = 0;
    for i in range(unos[len(unos)-1][0]+1,m):
            for j in range(0,n):
                if(t[i][j]!=0):
                    zero = 1;
                    break
    if(n-m>=2):
        print("Tiene infinitas soluciones")
    else:
        if(zero == 0):
            if (len(unos) == n-1):
                print("Con solucion")
            else:
                print("Tiene infinitas soluciones")
        else:
            print("Con solucion")
    
