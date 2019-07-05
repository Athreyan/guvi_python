num,rep=map(int,input().split())
lil=list(map(int,input().split()[:num]))
for i in range(0,num):
    if lil[i]==rep:
        print("yes")
        break
else:
    print("no")
