# Matrix multiplication implementation with error checking.
def matmul(A, B):
    
    # Find the matrices height and width (number of rows and number of columns).
    A_height, B_height = len(A), len(B)
    A_width, B_width = len(A[0]), len(B[0])
    
    # ADDITION: Type checking.
    if type(A) is not list or type(B) is not list:
        raise TypeError("Expected type 'array'.")

    # Check if the matrices are rectangular.
    for i in range(A_height):
        if len(A[i]) != A_width:
            raise Exception("Non-rectagular 2D array 'A': not a matrix.")

    for i in range(B_height):
        if len(B[i]) != B_width:
            raise Exception("Non-rectagular 2D array 'B': not a matrix.")

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
    [ 7,  8,  9],
    [10, 11, 12]
]

print(matmul(M1, M2))