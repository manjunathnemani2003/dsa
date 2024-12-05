nums=[5,1,1,2,3,4,5]
c=0

for i in range(len(nums)):
  for j in range(len(nums)):
    if i!=j:
      if nums[i]==nums[j]:
        nums[j]='_'

for i in nums:
  if isinstance(i,int):
    c=c+1

i=0
while i<len(nums):
  if nums[i]=="_":
    nums.remove(nums[i])
    i=0
  else:
    i=i+1

print(c)
print(nums)

