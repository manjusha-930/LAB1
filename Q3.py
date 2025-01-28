def matrix_power(matrix, m):
    # Checking if m is a positive integer
    if m <= 0:
        return "Exponent must be a positive integer"
    # Checking the matrix is square or not
    rows = len(matrix)
    for row in matrix:
        if len(row) != rows:
            return "Matrix must be square"
    # Initialize result as the identity matrix
    result = [[1 if i == j else 0 for j in range(rows)] for i in range(rows)]
    # Multiply the matrix m times
    for _ in range(m):
        # Perform matrix multiplication
        temp = [[0] * rows for _ in range(rows)]
        for i in range(rows):
            for j in range(rows):
                temp[i][j] = sum(matrix[i][k] * result[k][j] for k in range(rows))
        result = temp
    return result
# Example
A = [
    [1, 2],
    [3, 4]
]
m = 2

# Call the function
result = matrix_power(A, m)
print("A^m:")
for row in result:
    print(row)
