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
        
        self.is_square = (self.height == self.width)
    
    def __repr__(self):
        # Create the representation.
        r = "[\n"

        # Append each row.
        for i in range(self.height):
            r += str(self.data[i]) + ",\n"
        
        r = r[:-2]
        r += "]"

        # Final representation.
        return r
        
    def __str__(self):
        # Initalise array with the widths for each column.
        w = [0 for j in range(self.width)]

        # Find all the values.
        for j in range(self.width):
            column_width = 0
            for i in range(self.height):
                if len(str(self.data[i][j])) > column_width:
                    column_width = len(str(self.data[i][j]))
            w[j] = column_width

        # Create the representation.
        r = ""

        # Append the top.
        r += "┌" + " "*(sum(w)+2*len(w)) + "┐\n"

        # Append each row.
        for i in range(self.height):
            # Append spacing between the lines.
            if i != 0:
                r += "│" + " "*(sum(w)+2*len(w)) + "│\n"
        
            r += "│ "
            # Append each column
            for j in range(self.width):
                r += str(self.data[i][j]).ljust(w[j]+2)

            # Remove a redundant space.
            r = r[:-1]
            r += "│\n"

        # Append the bottom.
        r += "└" + " "*(sum(w)+2*len(w)) + "┘"

        # Final representation.
        return r
    
    def __mul__(self, other):
        # Type checking.
        if type(other) is not Matrix:
            raise TypeError("Expected type 'Matrix'.")

        # Check if the width in matrix 'self' is equal to the height of matrix 'other'.
        if self.width != other.height:
            raise Exception("Dimension mismatch: width of matrix 'self' not equal to height of matrix 'other'.")
        depth = self.width # other.height can also be used.

        # Initialise the output array with the correct dimensions.
        C = Matrix([[None for j in range(other.width)] for i in range(self.height)])

        # Iterate over each entry in 'C'.
        for i in range(self.height):
            for j in range(other.width):
                # Sum over the product of the entries in A and B.
                C.data[i][j] = sum(self.data[i][d]*other.data[d][j] for d in range(depth))

        # Return the calculated matrix.
        return C

    def __pow__(self, power):
        # Type checking.
        if type(power) is not int:
            raise TypeError("Expected type 'int'.")

        if power < 0:
            raise ValueError("Power must be non-negative.")

        if not self.is_square:
            raise Exception("Matrix must be square.")

        result = identity(self.width) # self.height can also be used

        for i in range(power):
            result *= self

        return result

    def __eq__(self, other):
        # Type checking.
        if type(other) is not Matrix:
            return False

        # Check if they are the same size.
        if self.height != other.height or self.width != other.width:
            return False
        
        # Check each index.
        for i in range(self.height):
            for j in range(self.width):
                if self.data[i][j] != other.data[i][j]:
                    return False
        
        # If it passes all the checks
        return True

    def __ne__(self, other):
        # It's that easy.
        return not self.__eq__(other)

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
    [19, 20, 21]
])

M5 = M1 * M2 * M3 * M4

print(M1 * M2 * M3 * M4 != M5)