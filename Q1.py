import numpy as np

numberOfMatrices , martabe = map(int , input().split())

matrices = []

for i in range(numberOfMatrices):
    matrix = []
    for j in range(martabe):
        s = list(map(int , input().split()))
        matrix.append(s)
    matrix = np.array(matrix)
    matrices.append(matrix)

maximumDeterminant = -1000000 * 100 * 100
pairWithMax = (-1 , -1)
detOfPair = (1000 * -100000 , 100000 * -1000)

for i in range(len(matrices)):
    for j in range(i + 1 , len(matrices)):
        m1 = matrices[i]
        m2 = matrices[j]
        d1 = np.linalg.det(m1)
        d2 = np.linalg.det(m2)

        det = d1 * d2
        if det > maximumDeterminant:
            maximumDeterminant = det
            pairWithMax = (i , j)
            detOfPair = (d1 , d2)

# we want to calculate  A * B
A , B = None , None

if detOfPair[0] >= detOfPair[1]:
    A = matrices[pairWithMax[0]]
    B = matrices[pairWithMax[1]]
else:
    B = matrices[pairWithMax[0]]
    A = matrices[pairWithMax[1]]

result = np.linalg.inv(np.matmul(A , B))

for i in range(martabe):
    for j in range(martabe):
        print(f'{result[i,j]:.3f}' , end=' ')
    print()