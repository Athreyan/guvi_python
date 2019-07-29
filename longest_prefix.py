def prefix(st1,st2):
  if(st1 in st2):
    return st1
  else:
    return prefix(st1[0:len(st1)-1],st2)
val=int(input())
lil=[]
for _ in range(0,val):
    lil.append(input())
lil.sort()
print(prefix(lil[0],lil[val-1]))
