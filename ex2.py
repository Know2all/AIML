import numpy as np
from numpy.linalg import det

def create_matrix():
    r, c = map(int, input("Enter the shape of the matrix (r, c): ").split())
    mat = np.zeros((r, c), int)
    for i in range(r):
        for j in range(c):
            mat[i, j] = int(input(f"Enter element at position ({i},{j}): "))
    return mat

def task1():
    mat = create_matrix()
    
    r, c = map(int, input("Enter the position of the element (r, c): ").split())
    pos = (r, c)
    print(f"Element at position {pos} is {mat[pos]}")
    
    if mat.shape[0] == mat.shape[1]:
        print(f"Determinant of the matrix: {det(mat)}")
    else:
        print("Matrix is not square, so determinant cannot be computed.")

def task2():
    mat = create_matrix()
    print("Matrix:\n", mat)
    
    start_row = int(input("Enter the start row: "))
    end_row = int(input("Enter the end row: "))
    start_col = int(input("Enter the start column: "))
    end_col = int(input("Enter the end column: "))
    
    subarray = mat[start_row:end_row, start_col:end_col]
    print(f"Subarray:\n{subarray}")
    print(f"Sum of the subarray: {np.sum(subarray)}")
    print(f"Mean of the subarray: {np.mean(subarray)}")
    print(f"Median of the subarray: {np.median(subarray)}")

class Matrix:
    @staticmethod
    def create_matrix():
        return create_matrix()
    
    @staticmethod
    def m_add(mat1, mat2):
        return np.dot(mat1, mat2)

def main():
    while True:
        print("\nSelect a task:")
        print("1. Task 1: Access element and compute determinant")
        print("2. Task 2: Extract subarray and compute statistics")
        print("3. Task 3: Scalar Multiplication")
        print("0. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            task1()
        elif choice == 2:
            task2()
        elif choice == 3:
            print("Creating first matrix:")
            mat1 = Matrix.create_matrix()
            print("Creating second matrix:")
            mat2 = Matrix.create_matrix()
            if mat1.shape[1] != mat2.shape[0]:
                print("Matrices cannot be multiplied due to incompatible shapes.")
            else:
                result = Matrix.m_add(mat1, mat2)
                print("Resultant matrix:\n", result)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
