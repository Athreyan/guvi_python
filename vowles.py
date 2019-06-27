word=input("Enter the charater :")
wrd=word.lower()
if len(wrd)>0 and wrd.isalpha():
	if wrd in 'aeiou':
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
