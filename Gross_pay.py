# Moaz Nabeel
A=float(input(" No. of Hours ? "))
B=float(input(" Rate Per Hour ? ($/hr)"))
if A<=40:
	Gross_pay=float(A)*float(B)
	print("Your Gross Pay Weekly is:" +str(Gross_pay))
elif 40 < A <= 168:
    Gross_pay=40*float(B)+(float(A)-40)*1.5*float(B)
    print("Your Gross Pay Weekly with bonus is:" +str(Gross_pay))

else:
	print(" There are only 168 hours in a Week !!!")      



 
