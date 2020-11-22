list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
value,k = map(int,input().split())
index = 0
while value>0:
    list[len(list)-1-index]=value%2
    value = value//2
    index = index + 1
if k<0:
    k = abs(k)
    while k>0:
        list.append(list[0])
        del list[0]
        k = k - 1
elif k>0:
    while k>0:
        list.insert(0,list[len(list)-1])
        del list[len(list)-1]
        k = k - 1
else:
    pass
sum = 0
for i in range(len(list)):
    sum = sum + list[len(list)-1-i]*2**i
print(sum)