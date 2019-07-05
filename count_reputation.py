num,rep=map(int,input().split())
lil=list(map(int,input().split()[:num]))
count=0
for i in range(0,num):
    if(lil[i]==rep):
        count=count+1
print(count)
