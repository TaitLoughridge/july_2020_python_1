User_input = int(input('Day of the week, Pick a number betweeen (0-6)? '))
Sunday = 0
Monday = 1
Tusday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saterday = 6

if User_input == Sunday:
    print("Sleep in")
if User_input == Monday:
    print("Go to work")
if User_input == Tusday:
    print("Go to work")
if User_input == Wednesday:
    print("Go to work")
if User_input == Thursday:
    print("Go to work")
if User_input == Friday:
    print("Go to work")
if User_input == Saterday:
    print("Sleep in")
if (User_input < 0) or (User_input > 6):
    print("You are out of range.")