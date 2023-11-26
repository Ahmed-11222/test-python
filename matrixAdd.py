matrix=[[1,5,1],
        [4,9,2],
        [5,6,3]]
matrix2=[[5,5,1],
        [5,8,1],
        [9,2,6]]
def add(matrix, matrix2):

    for i in range(len(matrix)):
        for j in range(len(matrix2)):
            x=matrix[i][j]+matrix2[i][j]
            print(x)

def main():
    add(matrix, matrix2)

main()

        