#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add_matrices(matrix1, matrix2):
    
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition.")

   
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]

  
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    return result


matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]


result_matrix = add_matrices(matrix_a, matrix_b)
 
print("Matrix A:")
for row in matrix_a:
    print(row)

print("\nMatrix B:")
for row in matrix_b:
    print(row)

print("\nResult Matrix:")
for row in result_matrix:
    print(row)


# In[ ]:




