arr=[24,1,26,29]
n=27
mind=float('inf')
m=[]

for i in range(len(arr)):
  if abs(n-arr[i])<mind:
    mind=abs(n-arr[i])
    m.append(arr[i])

print(m[-1])

