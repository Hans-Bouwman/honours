# Matrix multiplication implementation.
def matmul(A, B):
    # Find the matrices height and width (number of rows and number of columns).
    A_height, B_height = len(A), len(B)
    A_width, B_width = len(A[0]), len(B[0])
    
    # Initialise the output array with the correct dimensions.
    C = [[None for j in range(B_width)] for i in range(A_height)]

    # Interate over each entry in 'C'.
    depth = A_width # B_height can also be used.
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