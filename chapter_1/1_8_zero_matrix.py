def zero_matrix(matrix):
    rows = set()
    cols = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    for row in rows:
        for i in range(len(matrix[row])):
            matrix[row][i] = 0

    for col in cols:
        for i in range(len(matrix)):
            matrix[i][col] = 0


if __name__ == "__main__":
    m = [[0,1,2], [3,4,5], [6,0,7]]
    zero_matrix(m)
    print(m)
