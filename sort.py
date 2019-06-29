num=int(input())
dd=list(map(int,input().split()[:num]))
#aa=[]
'''while dd:
    min=dd[0]
    for i in dd:
        if i<min:
            min=i
        aa.append(min)
        #dd.remove(min)
print(aa)'''
for i in range(len(dd)):
    for j in range(i+1,len(dd)):
        if dd[i]>dd[j]:
            dd[i],dd[j]=dd[j],dd[i]
for a in range(len(dd)):
    print(dd[a],end=" ")
