size_input = input().split()
m = int(size_input[0])
n = int(size_input[1])

if m != n:
    print("rectangular matrix")
    print()
    matrix1 = []
    for i in range(m):
        row_input = input().split()
        row_list = []
        for num in row_input:
            row_list.append(int(num))
        matrix1.append(row_list)

    matrix2 = []
    for i in range(n):
        temp_row = []
        for j in range(m):
            temp_row.append(0)
        matrix2.append(temp_row)

    i = 0
    while i < m:
        j = 0
        while j < n:
            matrix2[j][i] = matrix1[i][j]
            j = j + 1
        i = i + 1

    print()
    print()
    i = 0
    while i < m:
        j = 0
        while j < n:
            print(matrix1[i][j], end=" ")
            j = j + 1
        print()
        i = i + 1

    print()
    print()
    i = 0
    while i < n:
        j = 0
        while j < m:
            print(matrix2[i][j], end=" ")
            j = j + 1
        print()
        i = i + 1

else:
    print("square matrix")
    print()
    matrix = []
    for i in range(m):
        row_input = input().split()
        row_list = []
        for num in row_input:
            row_list.append(int(num))
        matrix.append(row_list)

    print()
    print()
    i = 0
    while i < m:
        j = 0
        while j < m:
            print(matrix[i][j], end=" ")
            j = j + 1
        print()
        i = i + 1

    print()
    print()
    i = 0
    while i < m:
        j = 0
        while j < m:
            if i != j and i < j:
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            j = j + 1
        i = i + 1

    i = 0
    while i < m:
        j = 0
        while j < m:
            print(matrix[i][j], end=" ")
            j = j + 1
        print()
        i = i + 1