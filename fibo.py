lim=int(input())
f,s=0,1
while lim>0:
    f,s=s,f+s
    lim=lim-1
    print(f,end=' ')
