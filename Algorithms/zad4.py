from random import randint

matrix1 = []
matrix2 = []
for i in range(0, 128):
    matrix1.append([])
    matrix2.append([])
    for j in range(0, 128):
        matrix1[i].append(randint(0, 1000))
        matrix2[i].append(randint(0, 1000))

out_matrix = []
for i in range(0, 128):
    out_matrix.append([])
    for j in range(0, 128):
        out_matrix[i].append(matrix1[i][j] + matrix2[i][j])

