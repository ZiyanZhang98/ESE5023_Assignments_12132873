import numpy as np


def create_matrix():
    m1 = np.random.randint(0, 51, size=(5, 10))
    m2 = np.random.randint(0, 51, size=(10, 5))
    return m1, m2


def Matrix_multip(matrix_1, matrix_2):
    k = 0
    x = 0
    result = []
    row1, length1 = np.shape(matrix_1)
    row2, length2 = np.shape(matrix_2)
    for q in range(row1):
        for i in range(row1):
            for j in range(row2):
                x += int(matrix_1[k][j]) * int(matrix_2[j][i])
            result.append(x)
            x = 0
        k += 1
    return np.reshape(result, (5, 5))


if __name__ == '__main__':
    m1, m2 = create_matrix()
    print('Matrix 1:')
    print(m1, end='\n\n')
    print('Matrix 2:')
    print(m2)
    print(np.matmul(m1, m2))  # Output the correct answer calculated by built-in function
    print(Matrix_multip(m1, m2))  # Output reshaped matrix by our function
