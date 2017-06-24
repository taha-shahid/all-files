#Taha Shahid polynomial

n=raw_input("Enter X :")
n=int(n)

a=map(int,raw_input('Enter upto 5 coefficients ').split())
r=len(a)
num=a[0]*(n**r-1)+a[1]*(n**(r-2))+a[2]*(n**(r-3))+a[3]*(n**(r-4))+a[1]*(n**(r-5))
print num
