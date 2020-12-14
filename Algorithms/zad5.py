from random import randint

matrix1 = []
matrix2 = []
for i in range(0, 8):
    matrix1.append([])
    matrix2.append([])
    for j in range(0, 8):
        matrix1[i].append(randint(0, 1000))
        matrix2[i].append(randint(0, 1000))

out_matrix = []
for i in range(0, 8):
    out_matrix.append([])
    for j in range(0, 8):
        val = 0
        for k in range(0, 8):
            val += matrix1[i][k] * matrix2[k][j]
        out_matrix[i].append(val)

