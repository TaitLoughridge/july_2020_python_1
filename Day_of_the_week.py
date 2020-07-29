User_input = int(input('Day, Pick a number betweeen (0-6)? '))
Sunday = 0
Monday = 1
Tusday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saterday = 6

if User_input == Sunday:
    print("Sunday")
if User_input == Monday:
    print("Monday")
if User_input == Tusday:
    print("Tusday")
if User_input == Wednesday:
    print("Wednesday")
if User_input == Thursday:
    print("Thursday")
if User_input == Friday:
    print("Friday")
if User_input == Saterday:
    print("Saterday")
if (User_input < 0) or (User_input > 6):
    print("You are out of range.")


 #   def dayNumbers():    day = int(input("What day is it? "))    if day == 0:        print("Sunday")    elif day == 1:        print("Monday")    elif day == 2:        print("Tuesday")    elif day == 3:        print("Wednesday")    elif day == 4:        print("Thursday")    elif day == 5:        print("Friday")    elif day == 6:        print("Saturday")    else:        print("Not a day!")    dayNumbers()

 #   day = int(input('Day (0-6)? '))daysarr = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]print(daysarr[day])