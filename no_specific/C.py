n=int(input())
arr=list( map(int, input().split()) )
A=0
B=0
mylen=len(arr)
cntarr=arr
for i in range(0,mylen):
    for j in range(0,i+1):
        if arr[i]>=arr[j] and i%2==0:
            A=A+1
        if arr[i]>=arr[j] and i%2==1:
            B=B+1
        if arr[i]<arr[j] and i%2==0:
            A=A-1
        if arr[i]<arr[j] and i%2==1:
            B=B-1

if A>B:
    print('Calculus is hebei king!')
elif A<B:
    print('huaji is hebei king!')
else:
    print('hebei shuang king!')