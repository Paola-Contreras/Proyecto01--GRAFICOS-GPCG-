#Universidad del Valle de Guatemala 
#Gráficos por computador 
#Gabriela Paola Contreras Guerra 20213
#Libreria Matematica a utilizar 

#Function use to create a matrix, these is used based on a list that conteins all the data that I want on my matrix
#also it allows me to set the size of the matrix 
def createMatrix(row, column, List):
    mat = []
    for i in range(row):
        rowList = []
        for j in range(column):
            rowList.append(List[row * i + j])
        mat.append(rowList)
    return mat

#Function use to muliply 2 matrix using a comprehenshion list 
def multiplyMatrix(A,B):
    result = [[(sum(a * b for a, b in zip(B_row, A_col)))
                            for A_col in zip(*B)]
                                for B_row in A]
    return result

#Funtion use to multiply a matrix and a vector and save the result on a list 
def matmulvec(Matrix, vector):
    if len(Matrix[0]) != len(vector):
        return None
    result = []
    
    for i in range(len(Matrix)):
        suma = 0
        for j in range(len(Matrix[0])):
            suma += Matrix[i][j]*vector[j]
        result.append(suma)

    return result


#Dot product that gets 2 vectors 
#multiply each value and add the product of each multiplication to get the product
def dotProduct(a,b):
    dotproduct =0
    for a,b in zip(a,b):
        dotproduct = dotproduct +a*b
        d = dotproduct
    return d

#Cross product of 2 vectors 
def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]]

    return c
#Cross product of 2 vectors 
def cross2(a, b):
    c=[]
    for c in range(len(a), len(b)):
        c = [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]

    return c
#Substraction of vectors 
def subtract(a, b):
    result = [a[i] - b[i] for i in range(min(len(a), len(b)))]
    return result

#Function to get the length of the vector 
def normalize(v):
   length = pow(((v[0])**2 +(v[1])**2 +(v[2])**2 ),0.5)
   return length

#Get the transpose matrix 
def transpose(m):
    return list(map(list,zip(*m)))

def MMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

#Fin the determinant of the matrix 
def getdeterminant(m):
    #Use in 2 x 2 matrix 
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getdeterminant(MMinor(m,0,c))
    return determinant

#find matrix of cofactors
def inv(m):
    cofactors = []
    determinant = getdeterminant(m)
  
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = MMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getdeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors





# REFERENCES 
# -- https://www.anycodings.com/questions/matrix-inversion-without-numpy
