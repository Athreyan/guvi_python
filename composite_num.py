value=int(input())
for i in range(2,value):
    if value%i==0:
        print("yes")
        break
else:
    print("no")
