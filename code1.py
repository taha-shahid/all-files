#Taha Shahid

#Initial guess was that there is going to be a range of numbers that are going
#to be a set of numbers that will come close to the provided upper limit
#but break if the division of the first range and second range equals 0
#hence they have to be prime numbers

ul = input("Please enter a number as an upper limit:")
ul = int(ul)

for num in range(2,ul):
	prime = True
	for i in range(2,num):
		if (num%i) == 0:
			prime = False
	if prime:
		print(num)

print("Here are all the Prime Numbers below your given upper limit")
