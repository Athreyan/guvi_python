word=input("Enter the charater :")
wrd=word.lower()
if len(wrd)>0 and wrd.isalpha():
	if wrd in 'aeiou':
		print("VOWEL")
	else:
		print("Constant")
else:
	print("INVALID !!")
