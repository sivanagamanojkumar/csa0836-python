date = input("Enter the date to be checked: ")
day, month, year = map(int, date.split("/"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year,"is a Leap Year")
    next_leap_year = year + (4 - year % 4)
    print("Next Leap Year:", next_leap_year)
else:
    print(year ,"is not a Leap Year")
    previous_leap_year = year - (year % 4)
    print("Previous Leap Year:",previous_leap_year)
