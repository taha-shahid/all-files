#Taha Shahid

N = input("Please enter a number as an upper limit:")
N = int(N)

for i in range(2,N):
	prime = True
	for k in range(2,i):
		if (i%k) == 0:
			prime = False
	if prime:
		print(i)

print("Here are all the Prime Numbers Below your given upper limit")

