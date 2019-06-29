val1,val2=map(int,input().split())
l=len(str(val1))

for i in range(val1,val2):
    su=0
    su2=i
    while(su2!=0):
        su=su+((su2%10)**l)
        su2=su2//10
    if(su==i):
        print(i,end=" ")
   
