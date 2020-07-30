matrix_one = [ [1,3],[2,4] ]

matrix_two = [ [5,2],[1,0] ]

solution = [[0,0],[0,0]]

# print(matrix_one[0][0] + matrix_two[1][0])

# print(solution)

if len(matrix_one) == len(matrix_two):
    for i in range(len(matrix_one)):
        for j in range(len(matrix_two)):
            print(str(matrix_one[i][j]) + "+" + str(matrix_two[i][j]))

else:
    print("this matrix are not the same length")
