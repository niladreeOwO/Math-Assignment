print("Enter dimensions of Matrix 1:")
r1 = int(input("Rows: "))
c1 = int(input("Columns: "))

print("\nEnter dimensions of Matrix 2:")
r2 = int(input("Rows: "))
c2 = int(input("Columns: "))

if c1 != r2:
    print("\nError: Cannot multiply. Columns of Matrix 1 must equal rows of Matrix 2.")
    exit()

print("\nEnter values for Matrix 1 (row by row):")
matrix1 = []
for i in range(r1):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != c1:
        print("Error: Incorrect number of elements. Restart program.")
        exit()
    matrix1.append(row)

print("\nEnter values for Matrix 2 (row by row):")
matrix2 = []
for i in range(r2):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    if len(row) != c2:
        print("Error: Incorrect number of elements. Restart program.")
        exit()
    matrix2.append(row)

result = []
for i in range(r1):
    row = []
    for j in range(c2):
        total = 0
        for k in range(c1):
            total += matrix1[i][k] * matrix2[k][j]
        row.append(total)
    result.append(row)

print("\nMatrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nResult (Matrix 1 × Matrix 2):")
for row in result:
    print(row)
