#Question 1
sec=float(input("Please enter a number to represent seconds: "))
hours=sec//3600
minutes=sec%3600//60
secs=sec%3600%60
print("Hours:",hours,"\nMinutes:",minutes,"\nSeconds:",secs)

#Question 2
F=10000
r=.0299
n=10
P=F/(1+r)**n
print("You must invest",format(P,"4.2f"),"to get $10,000 in 10 years at a 2.99% APR.")
