name=list(input())
if len(name)%2==0:
    name[int(len(name)/2)]='*'
    name[int(len(name)/2)-1]='*'
else:
    name[int(len(name)/2)]='*'
for i in range(len(name)):
    print(name[i],end='')
