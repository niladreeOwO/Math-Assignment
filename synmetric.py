size_input = input().split()
m = int(size_input[0])
n = int(size_input[1])

count_check = 0

if m != n:
    print("not symmetric")
    exit()

matrix = []
for r in range(m):
    row_input = input().split()
    row_list = []
    for num in row_input:
        row_list.append(int(num))
    matrix.append(row_list)

i = 0
while i < m:
    j = 0
    while j < m:
        if matrix[i][j] == matrix[j][i]:
            count_check = count_check + 1
        j = j + 1
    i = i + 1

if count_check == m * m:
    print("symmetric")
    print()
    x = 0
    while x < m:
        y = 0
        while y < n:
            print(matrix[x][y], end=" ")
            y = y + 1
        print()
        x = x + 1
else:
    print("not symmetric")