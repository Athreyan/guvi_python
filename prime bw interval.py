b,e=map(int,input().split())
for i in range(b+1,e,1):
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                break

        else:
            print(i, end=" ")

        
