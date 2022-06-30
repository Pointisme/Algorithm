def matrix_mult(A, B):  #행렬 곱 정의
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j])   #행렬의 곱 형태니까 (i*k)(k*j)=(i*j)의 형식 
    return temp

def matrix_pow(n, M):
    if n == 1:  #마무리
        return M
    if n % 2 == 0:  #짝수일때
        temp = matrix_pow(n//2, M)
        return matrix_mult(temp, temp)
    else:   #홀수일때
        temp = matrix_pow(n-1, M)
        return matrix_mult(temp, M)

A = [[1, 1], [1, 0]]
print(matrix_pow(9, A)[0][0])