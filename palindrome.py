num=int(input())
rev=0
num2=num
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(num2==rev):
    print("yes")
else:
    print("no")
        
     
    

