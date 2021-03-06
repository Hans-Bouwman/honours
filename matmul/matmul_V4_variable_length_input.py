# Matrix multiplication implementation with error checking and variable length input

# ADDITION: variable input length function
def matmul(*args):

    # Return 'None' if no input is given (raising an error would also be appropriate).
    if len(args) == 0: return None

    # Reformat the input (necessary due to wrapping in a tuple by recursion).
    if len(args) == 1 and type(args[0] is tuple): args = args[0]
    
    # CHANGE: Reworked type checking.
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

print(matmul(M1, M2, M3, M4))