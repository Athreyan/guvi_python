
    
from itertools import combinations
num1,num2=map(int,input().split())
le=len(str(num1))
l=list(combinations(str(num1),le-num2))
#print(l)
l=(sorted(l))
#print(l)
y="".join(l[0])
print(y)

