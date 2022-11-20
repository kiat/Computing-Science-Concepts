



def multiply_matrix(A, B):
    C = [[0 for x in range(len(A))] for y in range(len(B[0]))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C



def main():

    # Let us test it
    # input two matrices of size n x m
    A = [[2, 0, 0],
         [0, 2, 0],
         [0, 0, 2]]
    
    B = [[2, 2, 2],
         [2, 2, 2],
         [2, 2, 2]]

    

    C = multiply_matrix(A, B)
    print(C)

if __name__ == "__main__":
    main()
