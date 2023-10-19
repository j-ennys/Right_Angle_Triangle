# main routine starts here

# set maximum number of tickets below
MAX_PROBLEMS = 4

# loop to sell tickets
problems_sold = 0
while problems_sold < MAX_PROBLEMS:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    problems_sold += 1

# Output number of tickets sold
if problems_sold == MAX_PROBLEMS:
    print("Congratulations! You have complete all the problems ")
else:
    print("You have complete {} problem/s. There is {} problem/s "
          "remaining".format(problems_sold, MAX_PROBLEMS - problems_sold))