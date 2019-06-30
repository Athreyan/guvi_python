num=int(input())
lil=list(map(int,input().split()[:num]))
for i in range(num):
    print(lil[i],i)
