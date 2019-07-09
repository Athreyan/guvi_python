num=int(input())
rev=0
h=0
while num>0:
    h=num%10
    rev=(rev*10)+ h
    num=num//10
    
print(rev)
