## Functionality

The script first prompts the user for the dimensions (rows and columns) of the two matrices. It then checks if the matrices have identical dimensions, as this is a prerequisite for addition.

If the dimensions are compatible, the program reads the elements of both matrices, displays both input matrices, and finally displays the resulting sum matrix. If the dimensions are incompatible (e.g., trying to add a 2x3 matrix to a 3x2 matrix), the program prints "invalid" and exits.

## Input Format

The program expects sequential input from the user:

1. **Dimensions:** A single line containing four space-separated integers: `Rows1`, `Cols1`, `Rows2`, `Cols2`.

2. **Matrix 1 Elements:** `Rows1` lines, each containing `Cols1` space-separated integers.

3. **Matrix 2 Elements:** `Rows2` lines, each containing `Cols2` space-separated integers.

### Example Input
2 2 2 2
1 2
3 4
5 6
7 8


## Output Format

The output includes the initial prompt for dimensions, followed by the complete display of the first matrix, the second matrix, and the final sum matrix. Each matrix display is separated by two blank lines.

### Example Output
1 2 
3 4 


5 6 
7 8 


6 8 
10 12 

