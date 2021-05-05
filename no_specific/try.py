num=input()
if num[0]=='-':
    for i in num:
        if i!='-':
            print(i,end="")
else:
    print("-"+str(num))