def matrixElementsSum(matrix):
    cost = 0
    flag = 1000000
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            print('i,j :',i,j)
            if matrix[i][j] == 0:
                temp = i
                while temp<(len(matrix)-1):
                    matrix[i+1][j]=0
                    temp = temp + 1
                flag = j
                print('if ',flag)
                print('cost ',cost,'\n')
                continue
            elif j == flag:
                print('elif ',flag)
                print('cost ',cost,'\n')
                continue
            else:
                print('else',flag)
                cost = cost + matrix[i][j]
                print('cost ',cost,'\n')
    return cost

if __name__ == '__main__':
		print('''
find the total cost. If the value of troom is 0 it is haunted it cant be used along with room below it. Count val for column value w/o zero.
		''')
		matrix = [[1, 1, 1, 0], 
							[0, 5, 0, 1], 
							[2, 1, 3, 10]]
		cost = matrixElementsSum(matrix)
		print(cost)