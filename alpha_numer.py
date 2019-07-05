val=input()
for v in range(0,len(val)):
    
    if (val[v].isalpha() and val[v].isnumeric()):
        print("No")
else:
        print("Yes")
