from random import randint

n = randint(0, 10)
matrix1 = []

for i in range(0, n):
    matrix1.append([])
    for j in range(0, n):
        matrix1[i].append(randint(0, 10))

for m in matrix1:
    print(m)


def recursive(matrix):
    ind = list(range(len(matrix)))
    if len(matrix) == 1:
        determinant = matrix[0][0]
        return determinant
    elif len(matrix) == 2:
        determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return determinant

    determinant = 0
    for pos in ind:
        mat_copy = copy(matrix)
        mat_copy = mat_copy[1:]
        height = len(mat_copy)
        for i in range(height):
            mat_copy[i] = mat_copy[i][0:pos] + mat_copy[i][pos+1:]

        sign = (-1)**(pos % 2)
        int_determinant = recursive(mat_copy)
        determinant += sign * matrix[0][pos] * int_determinant

    return determinant


def copy(matrix):
    ret_mat = []
    for i in range(len(matrix)):
        ret_mat.append([])
        for j in range(len(matrix)):
            ret_mat[i].append(matrix[i][j])
    return ret_mat


det = recursive(matrix1)
print(det)

