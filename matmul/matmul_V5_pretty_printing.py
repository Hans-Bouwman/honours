# Matrix multiplication implementation with error checking and variable length input
def matmul(*args):
    
    # Return 'None' if no input is given (raising an error would also be appropriate).
    if len(args) == 0: return None

    # Reformat the input (necessary due to wrapping in a tuple by recursion).
    if len(args) == 1 and type(args[0] is tuple): args = args[0]
    
    # Type checking.
    for arg in args:
        if type(arg) is not list:
            raise TypeError("Expected type 'array'.")

    # Return the matrix if it's the only input.
    if len(args) == 1: return args[0]

    # Recursively compute if necessary.
    if len(args) >= 3: return matmul(matmul(args[0:-1]), matmul((list(args[-1]),)))
    
    # Normal computation
    A, B = args[0], args[1]

    # Find the matrices height and width (number of rows and number of columns).
    A_height, B_height = len(A), len(B)
    A_width, B_width = len(A[0]), len(B[0])
    
    # Check if the matrices are rectangular.
    for i in range(A_height):
        if len(A[i]) != A_width:
            raise Exception("Non-rectagular array 'A': not a matrix.")

    for i in range(B_height):
        if len(B[i]) != B_width:
            raise Exception("Non-rectagular array 'B': not a matrix.")

    # Check if the width in matrix 'A' is equal to the height of matrix 'B'.
    if A_width != B_height:
        raise Exception("Dimension mismatch: width of matrix 'A' not equal to height of matrix 'B'.")
    
    depth = A_width # B_height can also be used.

    # Initialise the output array with the correct dimensions.
    C = [[None for j in range(B_width)] for i in range(A_height)]

    # Iterate over each entry in 'C'.
    for i in range(A_height):
        for j in range(B_width):
            # Sum over the product of the entries in A and B.
            C[i][j] = sum(A[i][d]*B[d][j] for d in range(depth))
    
    # Return the calculated matrix.
    return C

def printm(M):
    # Type checking.
    if type(M) is not list:
            raise TypeError("Expected type 'array'.")

    # Find the matrices height and width (number of rows and number of columns) (borrowed).
    M_height = len(M)
    M_width = len(M[0])

    # Check if the matrix is rectangular (borrowed).
    for i in range(M_height):
        if len(M[i]) != M_width:
            raise Exception("Non-rectagular array 'A': not a matrix.")

    # Array with the widths for each column.
    W = [0 for j in range(M_width)]
    for j in range(M_width):
        reqw = 0
        for i in range(M_height):
            if len(str(M[i][j])) > reqw: reqw = len(str(M[i][j]))
        W[j] = reqw

    # Print the matrix.

    # 1) Print the top.
    print("┌" + " "*(sum(W)+2*len(W)) + "┐")
    
    # 2) Print each row.
    for i in range(M_height):

        # Print spacing between the lines.
        if i != 0:
            print("│" + " "*(sum(W)+2*len(W)) + "│")
        
        row = "│ "

        # Append each column
        for j in range(M_width):
            row += str(M[i][j]).ljust(W[j]+2)

        row = row[:-1]
        row += "│"
        print(row)

    # 3) Print the bottom.
    print("└" + " "*(sum(W)+2*len(W)) + "┘")

# Test
M1 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

M2 = [
    [ 7,  8,  9, 10],
    [11, 12, 13, 14]
]

M3 = [
    [15],
    [16],
    [17],
    [18]
]

M4 = [
    [19, 20]
]

printm(matmul(M1, M2, M3, M4))