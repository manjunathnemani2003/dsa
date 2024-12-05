m=[]
n=[]
'''Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]'''
matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in matrix:
  for j in i:
    m.append(j)

z=0
while z<len(m):
  for i in range(len(matrix[0])-1):
    n.append(matrix[0][i])
    z=z+1
  for i in range(len(matrix)-1):
    n.append(matrix[i][-1])
    z=z+1
  for i in range(len(matrix[-1])-1):
    n.append(matrix[-1][-i-1])
    z=z+1
  for i in range(len(matrix)-1):
    n.append(matrix[-i-1][0])
    z=z+1


print(n)




