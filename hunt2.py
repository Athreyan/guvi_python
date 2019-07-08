num=int(input())
l=list(map(int,input().split()[:num]))
dd=0
l.sort(reverse=True)
for j in l:
    dd=dd*10+j
print(dd)
'''for i in range(num):
    dd.append(max(l))
    
    l.remove(max(l))
for k in dd:
    print(k,end='')'''
    
