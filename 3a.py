n=int(input("enter a num:"))
lis=[]
for i in range(1,n+1):
    if n%i==0:
        lis.append(i)
        print(lis)
