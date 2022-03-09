#trace of a matrix
trace=lambda M:sum(M[i][i] for i in range(len(M)))
# transpose of a matrix
trans=lambda M:[[M[k][i] for k in range(len(M))] for i in range(len(M[0]))]
#dotproduct of two vectors
dotproduct=lambda v1,v2:sum([v1[i]*v2[i] for i in range(len(v1))])
#dotproduct when F=C
Cdotproduct=lambda v1, v2:sum([v1[i]*v2[i].conjugate() for i in range(len(v1))])
#matrix multiplication
mmultiply=lambda M1,M2: [[dotproduct(k,i) for k in trans(M2)] for i in M1]
# determinant of a matrix
def determinant(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    return sum([(-1)**i*matrix[0][i]*determinant([k[:i]+k[:i:-1][::-1] for k in matrix[1:]]) for i in range(len(matrix))])
print(Cdotproduct([3+4j],[3+4j]))