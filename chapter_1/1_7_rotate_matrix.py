def rotate_matrix(matrix):

    n = len(matrix)

    for layer in range(n//2):
        start = layer
        end = n-1-layer

        for i in range(start, end):
            offset = i - start
            top = matrix[start][i]
            matrix[start][i] = matrix[end-offset][start]
            matrix[end-offset][start] = matrix[end][end-offset]
            matrix[end][end-offset] = matrix[i][end]
            matrix[i][end] = top

    return True

if __name__ == "__main__":
    m = [[1,2,3], [4,5,6], [7,8,9]]
    rotate_matrix(m)
    print(m)