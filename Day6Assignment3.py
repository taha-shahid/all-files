"Elizabeth Ringhausen"

N = input("Please enter a number as an upper limit:")
N = int(N)

for i in range(2,N):
    check_var = True
    for k in range(2,i):
        if (i%k) == 0:
            check_var = False
    if check_var:
        print(i)

print("All prime numbers that exist up to the entered limit are listed")
        
