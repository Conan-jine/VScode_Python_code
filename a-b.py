arr=input()
num=arr.split()
nums=[0,0]
i=0
for it in num:
    nums[i]=it
    i=i+1
print(nums[0]-nums[1])