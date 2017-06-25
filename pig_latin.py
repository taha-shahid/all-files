

def piglatin():
	vowellist=('a','e','i','o','u','A','E','I','O','U')
	word=raw_input("Please enter a single word: ")
	word1=word.lower()
	

	if word1[0] in vowellist:
		
		print word + 'hay' 
		
	else:
		print word[1:]+word[0]+'ay'

piglatin()
	

