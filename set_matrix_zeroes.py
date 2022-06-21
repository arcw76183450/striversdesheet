def set_all_zeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    setm = set()
    setn = set()
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                setm.add(row)
                setn.add(col)

    for a in range(m):
        for b in range(n):
            if a in setm or b in setn:
                matrix[a][b] = 0

    return matrix


matrix = [[2, 3, 2], [3, 0, 1], [4, 1, 0]]
print(set_all_zeroes(matrix))
