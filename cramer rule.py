

import numpy as np

def solve_system(matrix):
    n = len(matrix)  # Size of the matrix

    # Printing matrix A
    print("A=")
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

    # Determinant of A
    determinant_A = np.linalg.det(matrix)
    print("Determinant of A=", "{:.0f}".format(determinant_A))

    if determinant_A != 0:
        def input_column_matrix():
            B = []
            print("Enter the elements of the B matrix (one element per line):")
            try:
                # Get user input for each element
                for i in range(n):
                    element = float(input(f"Enter element {i + 1} of the B matrix: "))
                    B.append(element)  # Assuming elements are floats
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
            return B

        B = input_column_matrix()
        print("B=", B)

        # Make column_matrix a 2D array
        B = np.array(B).reshape(-1, 1)

        # Create arrays for A_x1, A_x2, A_x3, etc. by replacing the columns of A with B
        A_matrices = []
        for i in range(n):
            A_temp = [row[:] for row in matrix]  # Create a copy of matrix
            for j in range(n):
                A_temp[j][i] = B[j][0]
            A_matrices.append(A_temp)

            print(f"Matrix A_x{i+1}:")  # Printing A_x1, A_x2, A_x3, ...
            for row in A_temp:
                for element in row:
                    print(element, end="\t")
                print()

        # Determinant of A_x1, A_x2, A_x3, etc.
        determinants_A = [np.linalg.det(A) for A in A_matrices]

        for i, determinant_Ai in enumerate(determinants_A):
            print(f"Determinant of A_x{i+1}=", "{:.0f}".format(determinant_Ai))

        # Calculate and print the values of x1, x2, x3, ...
        variables = []
        for i, determinant_Ai in enumerate(determinants_A):
            variable = determinant_Ai / determinant_A
            variables.append(variable)
            print(f"The value of x{i+1} =", "{:.2f}".format(variable))

    elif determinant_A == 0:
        print("Matrix is singular.")

# Ask the user for the size of the system (n × n)
while True:
    try:
        n = int(input("Enter the size of the system (n): "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Loop to ask the user for the matrix elements
matrix = []
for i in range(n):
    new_row = input(f"Enter values for row {i + 1} with spaces between them: ")
    row = [float(x) for x in new_row.split()]
    matrix.append(row)

# Solve the system
solve_system(matrix)

# Ask if the user wants to run the code for another system
while True:
    run_again = input("Do you want to run the code for another system? (yes/no): ")
    if run_again.lower() != "yes":
        break

    # Ask for the size of the new system
    while True:
        try:
            n = int(input("Enter the size of the system (n): "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Ask for the matrix elements of the new system
    matrix = []
    for i in range(n):
        new_row = input(f"Enter values for row {i + 1} with spaces between them: ")
        row = [float(x) for x in new_row.split()]
        matrix.append(row)

    # Solve the new system
    solve_system(matrix)