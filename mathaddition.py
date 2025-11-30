def matrix_addition_exact():
    print("Enter row and column of 1st and 2nd matrix respectively")
    
    try:
        dims = list(map(int, input().split()))
        if len(dims) < 4:
            return
        m, n, o, p = dims
    except:
        return

    if m != o or n != p:
        print("invalid")
        return

    def read_matrix(rows, cols):
        mat = []
        for i in range(rows):
            try:
                row_input = list(map(int, input().split()))
                if len(row_input) == cols:
                    mat.append(row_input)
                else:
                    return None 
            except:
                return None
        return mat

    mat1 = read_matrix(m, n)
    if mat1 is None: return

    mat2 = read_matrix(o, p)
    if mat2 is None: return

    def print_matrix(matrix):
        for row in matrix:
            print(*(str(x) for x in row), end=" ")
            print()

    print_matrix(mat1)

    print()
    print()

    print_matrix(mat2)

    print()
    print()

    for i in range(m):
        for j in range(n):
            print(mat1[i][j] + mat2[i][j], end=" ")
        print()

if __name__ == "__main__":
    matrix_addition_exact()  
