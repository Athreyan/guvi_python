value1=int(input("Enter the first value :"))
value2=int(input("Enter the second value :"))
value3=int(input("Enter the third value :"))
if(value1>value2 and value1>value3):
	print(value1)
elif(value2>value3):
	print(value2)
else:
	print(value3)