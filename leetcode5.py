'''input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]'''

matrix=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
q=len(matrix)

n=[]
m=[]
for i in range(len(matrix)):
    for j in range(1,len(matrix)+1):
      m.append(matrix[-j][i])

j=0
c=0
p=[]
matrix.clear()
while j<len(m):
  p.append(m[j])
  c=c+1
  if c%q==0:
    matrix.append(p)
    p=[]
  j=j+1

print(matrix)

