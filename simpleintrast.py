p=int(input("enter the amount:"))
t=int(input("enter number of years:"))
age=int(input("enter age:"))
if (age>=50):
    print("intrest is",(p*t*10)/100)
elif (age<=50):
    print("intrest is ",(p*t*12)/100)
