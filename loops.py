title = "Cats are Awesome"
counter = 0

# this next variable will increment
 # while counter < len(title):
  #   if (counter % 2) == 0:
  #       print(title[counter])
  #   counter += 1

# a difert way to do every other
 # while counter < len(title):
 #     print(title[counter])
 #     counter += 2

# will remove blanks
while counter < len(title):
    if (counter % 2) == 0 and title[counter] != " ":
        print(title[counter])
    counter += 1