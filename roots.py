#Taha Shahid

import math as m
def roots():
	a=input('input a: ')
	b=input('input b: ')
	c=input('input c: ')
	d=(b**2)-(4*a*c)
	if d<0:
		print "Imaginary error"
	elif d==0:
		d01=(-b+m.sqrt(d))/(2*a)
		d02=(-b-m.sqrt(d))/(2*a)
		if d01==d02:
			print "only one root: "+ str(d01)
	else:
		dpos=(-b+m.sqrt(d))/(2*a)
		dneg=(-b-m.sqrt(d))/(2*a)
		print "First root: "+ str(dpos)
		print "Second root: "+ str(dneg)
roots()

