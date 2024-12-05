arr=[1,2,3,4,-5,1,2,3,5]
length=9

def find_negative(arr):
  for i in range(len(arr)):
    if arr[i]<0:
      return i

n=find_negative(arr)

a=0
for i in range(n):
  a=a+arr[i]

b=0
for i in range(n+1,len(arr)):
  b=b+arr[i]

if a>b:
  print(a)
else:
  print(b)



