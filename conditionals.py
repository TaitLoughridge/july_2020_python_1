user_input = int(input("Guess a number: "))
magic_Number = 35

if user_input == magic_Number:
    print("ARE YOU A MIND READER!?!?!?")
elif user_input > 50:
    print("Guess was too High")
elif user_input < 20:
    print("Guess was too low")
else:
    print("Sorry. Try again.")