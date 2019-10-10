def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Input matrix:")
    for row in matrix:
        print(row)
    transposed_matrix = transpose_matrix(matrix)
    print("Transposed matrix:")
    for row in transposed_matrix:
        print(row)

def transpose_matrix(matrix):
    N = len(matrix)
    M = len(matrix[0])
    # Length of first row will suffice because in matrices, 
    # len(matrix[0]) == len(matrix[N])

    # Works for square and rectangular matrices
    transposed_matrix = [
        [matrix[column][row] for column in range(N)] for row in range(M)
    ]
    
    # Works for square matrices only
    # for i in range(M):
    #     for j in range(N):
    #         transposed_matrix[i][j] = matrix[j][i]
    return transposed_matrix

if __name__ == '__main__':
    main()