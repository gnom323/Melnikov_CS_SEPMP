import numpy as np
n = int(input('N = '))
m = int(input('M = '))
matrix = np.zeros((n, m), dtype='int32')

num = n * m
res = 1
i = 0
j = 0
rotates = 0
next = 0
glob = 0
while(res <= num):
    if(next != 0 or i == n - 1 or j == m - 1):
        matrix = np.rot90(matrix, 1)
        
        rotates += 1
        i = rotates // 4
        j = rotates // 4
        next = 0
    elif(rotates % 2 == 1): 
        if(matrix[j][i] == 0): 
            matrix[j][i] += res
            res += 1
        if(i != n - 1): 
            next = matrix[j][i + 1]
        i += 1
    elif(rotates % 2 == 0): # четное число поворотов
        if(matrix[i][j] == 0): 
            matrix[i][j] += res 
            res += 1
        if(j != m - 1): 
            next = matrix[i][j + 1]
        j += 1
        
    print(matrix)
    if(res > 7):
        pass

matrix = np.rot90(matrix, 4 - (rotates % 4))
print(matrix)