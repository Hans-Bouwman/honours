# Matrix multiplication implementation with error checking and variable length input
def matmul(*args):
    
    # Return 'None' if no input is given (raising an error would also be appropriate).
    if len(args) == 0: return None

    # Reformat the input (necessary due to wrapping in a tuple by recursion).
    if len(args) == 1 and type(args[0] is tuple): args = args[0]
    
    # Type checking.
    for arg in args:
        if type(arg) is not Matrix:
            raise TypeError("Expected type 'Matrix'.")

    # Return the matrix if it's the only input.
    if len(args) == 1: return args[0]

    # Recursively compute if necessary.
    if len(args) >= 3: return matmul( matmul(args[0:-1]), matmul(([args[-1]]),) )
    
    # Normal computation
    A, B = args[0], args[1]

    # Check if the width in matrix 'A' is equal to the height of matrix 'B'.
    if A.width != B.height:
        raise Exception("Dimension mismatch: width of matrix 'A' not equal to height of matrix 'B'.")
    
    depth = A.width # B_height can also be used.

    # Initialise the output array with the correct dimensions.
    C = [[None for j in range(B.width)] for i in range(A.height)]

    # Iterate over each entry in 'C'.
    for i in range(A.height):
        for j in range(B.width):
            # Sum over the product of the entries in A and B.
            C[i][j] = sum(A.data[i][d]*B.data[d][j] for d in range(depth))
    
    # Return the calculated matrix.
    return Matrix(C)

def printm(M):
    
    # Type checking.
    if type(M) is not Matrix:
            raise TypeError("Expected type 'Matrix'.")

    # Initalise array with the widths for each column.
    w = [0 for j in range(M.width)]

    # Find all the values.
    for j in range(M.width):
        column_width = 0
        for i in range(M.height):
            if len(str(M.data[i][j])) > column_width:
                column_width = len(str(M.data[i][j]))
        w[j] = column_width

    # Print the matrix.
    
    # 1) Print the top.
    print("┌" + " "*(sum(w)+2*len(w)) + "┐")

    # 2) Print each row.
    for i in range(M.height):

        # Print spacing between the lines.
        if i != 0:
            print("│" + " "*(sum(w)+2*len(w)) + "│")
        
        row = "│ "

        # Append each column
        for j in range(M.width):
            row += str(M.data[i][j]).ljust(w[j]+2)
            
        # Remove a redundant space.
        row = row[:-1]
        row += "│"
        print(row)
    
    # 3) Print the bottom.
    print("└" + " "*(sum(w)+2*len(w)) + "┘")

class Matrix():
    def __init__(self, data):
        self.data = data

        if type(data) is not list:
            raise TypeError("Expected input of type 'array'.")

        self.height = len(data)

        for i in range(self.height):
            if type(data[i]) is not list:
                raise TypeError("Expected array elements of type 'array'.")

        self.width = len(data[0])
        
        for i in range(self.height):
            if len(data[i]) != self.width:
                raise Exception("Non-rectagular 2D-array: cannnot create matrix.")

# Test
M1 = Matrix([
    [1, 2],
    [3, 4],
    [5, 6]
])

M2 = Matrix([
    [ 7,  8,  9, 10],
    [11, 12, 13, 14]
])

M3 = Matrix([
    [15],
    [16],
    [17],
    [18]
])

M4 = Matrix([
    [19, 20]
])

printm(matmul(M1, M2, M3, M4))