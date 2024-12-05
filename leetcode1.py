nums=[1,2,2,1,-1]

if len(nums)==1:
  print(nums[0])

c=0
if len(nums)==3: 
  if nums[1]==nums[0]:
    print(nums[2])
  elif nums[1]==nums[2]:
    print(nums[0])
  else:
    print(nums[1])



for i in range(len(nums)):
  for j in range(len(nums)):
    if i!=j:
      if nums[i]!=nums[j]:
        c=c+1
  if c==len(nums)-1:
    print(nums[i])
  c=0
print(c)

