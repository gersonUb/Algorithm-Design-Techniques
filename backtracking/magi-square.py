import numpy as np

def print_matrix(matrix, n):
    print(np.array(matrix).reshape((n, n)))

def is_square_magic(matrix, n):
    number_magic = n * (n**2 + 1) // 2

    for i in range(n):
        row = matrix[i * n : (i + 1) * n]
        if sum(row) != number_magic:
            return False
    for j in range(n):
        if sum(matrix[i * n + j] for i in range(n)) != number_magic:
            return False

    if sum(matrix[i * n + i] for i in range(n)) != number_magic:
        return False
    if sum(matrix[i * n + (n - 1 - i)] for i in range(n)) != number_magic:
        return False

    return True


def magi_square(matrix, n, available):
    number_magic = n * (n**2 + 1) // 2

    if len(matrix) == n * n:
        if is_square_magic(matrix, n):
            print("Matriz mágica:")
            print_matrix(matrix, n)
        return
    
    for i in range(0,n**2):
        if available[i]:
            continue
        matrix.append(i+1)
        available[i] = True
        if len(matrix) == n:
            if sum(matrix) != number_magic:
                matrix.pop()
                available[i] = False
                continue
        magi_square(matrix, n, available)
        matrix.pop()
        available[i] = False

matrix = []
available = [False] * 9
n = 3

magi_square(matrix, n, available)