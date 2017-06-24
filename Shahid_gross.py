#Taha Shahid

rate=float(input(" What is your rate of pay? "))
hours=float(input( " How many hours did you work this week? "))

if hours == 0:
	gross= float(rate)*float(hours)
	print("No hours worked, no money given")
elif hours <= 40:
	gross1= float(rate)*float(hours)
	print("Your gross pay is:" +str(gross1))
elif 40 < hours <= 168:
	gross2= 40*float(rate)+(float(hours)-40)*1.5*float(rate)
	print("Your gross pay is:" +str(gross2))
else:
	print( "Sorry, there are not that many hours in a week")
