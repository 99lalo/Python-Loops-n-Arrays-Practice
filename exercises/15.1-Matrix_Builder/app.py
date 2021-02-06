#Import random
import random
#Create the function below:
def matrixBuilder(size):
    matrix_line = [1 for i in range(size)]
    matrix =[matrix_line for i in range(size)]
    return matrix
print(matrixBuilder(5))