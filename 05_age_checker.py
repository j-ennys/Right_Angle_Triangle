# functions go here

# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# Main routine goes here
problems_sold = 0

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 16 <= age <= 21:
        pass
    elif age < 16:
        print("Sorry you are too young for this problem solver")
        continue
    else:
        print("?? That looks like a typo, please try again. ")
        continue

    problems_sold += 1

print("You have sold {} problem/s".format(problems_sold))