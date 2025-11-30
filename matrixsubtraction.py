print("Enter row and column of 1st and 2nd matrix respectively")
m, n, o, p = map(int, input().split())

if m != o or n != p:
    print("invalid")
    exit()

mat1 = []
for i in range(m):
    row = list(map(int, input().split()))
    mat1.append(row)

mat2 = []
for i in range(o):
    row = list(map(int, input().split()))
    mat2.append(row)

for i in range(m):
    for j in range(n):
        print(mat1[i][j], end=" ")
    print()

print()
print()

for i in range(o):
    for j in range(p):
        print(mat2[i][j], end=" ")
    print()

print()
print()

for i in range(m):
    for j in range(n):
        print(mat1[i][j] - mat2[i][j], end=" ")
    print()