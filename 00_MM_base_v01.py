import pandas
from datetime import date

# functions go here

# shows instructions
def show_instructions():
    print(''''\n
****** Instructions ******

Enter the name or 'xxx' to quit - 

Age - (limitation 16<x<21)

Choose you want to find out angle(degree) or length right-angle triangle / triangle

For right-angle triangle, enter ...
- Enter values (only digit valid)
- Age (between 16 and 22)
- Choose calculate angle or length
_ Type of unknown value (angle/degree or length or both)

For right-angle triangle calculate angle ...
- Enter the length of the opposite side
- Enter the length of the adjacent side

For right-angle triangle calculate length ...
- Enter the length of the known side
- Enter the known angle in degrees 

For triangle calculate angle ...
- Enter the length of side opposite 
- Enter the length of side adjacent
- Enter the length of side hypotenuse 

For triangle calculate length ...
- Enter which side want to calculate (unknown value) - opposite / adjacent / hypotenuse
- Enter angle A in degrees
- Enter the length of side ----
- Enter the length of side ---

When you have entered all the users, press 'xxx' to quit.

The program will then display the length or angles details 
including the current date 

This information will also be automatically written to 
a text file.

***********************''')



# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank and only integers valid. Please try again")
        else:
            return response

def number_check(question):
   while True:
       response = input(question)


       # if the response is blank, outputs error
       if response == "":
           print("Sorry this can't be blank. Please try again")
       elif response.isdigit():
           print("Sorry this can't enter a number. Please try again")
       else:
           return response


# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")

# main routine starts here


# checks that users enter a valid response (eg yes / no
# angle/degree or length or both) based on list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}, This can't be blank or digit.".format(valid_responses[0], valid_responses[1])

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# set maximum number of problems below
MAX_PROBLEMS = 6
problems_sold = 0

yes_no_list = ["yes", "no"]
method_list = ["angle", "degree", "length", "both"]

# Lists to hold problem details
all_names = []

# Dictionary used to create frame ie: column_name:list
right_angle_triangle_dict = {
    "Name": all_names
}

# Ask user if they want to see the instructions
want_instructions = string_checker("Do you want to read instructions? (y/n) : ", 1, yes_no_list)

if want_instructions == "yes":
    show_instructions()

print()

# loop to sell problems
while problems_sold < MAX_PROBLEMS:
    name = number_check("Please enter your name or 'xxx' to quit: ")

    # exit loop if users type 'xxx' and have sold at least
    # one problem
    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must solve at least ONE problem before quitting")
        continue

    age = num_check("Age: ")

    # check user is between 16 and 21 (inclusive)
    if 16 <= age <= 21:
        pass
    elif age < 16:
        print("Sorry you are too young for this problem solver. This is for 16 to 21 user to understand program.")
        continue
    else:
        print("?? That looks like a typo, please try again. This is for 16 to 21 user to understand program.")
        continue

    # get payment method
    problem_method = string_checker("Choose a method (angle/degree or length or both) : ", 2, method_list)

    problems_sold += 1

  # add problem name, cost and surcharge to lists
    all_names.append(name)

# create data frame from dictionary to organise information
right_angle_triangle_frame = pandas.DataFrame(right_angle_triangle_dict)

# set index at end (before printing)
right_angle_triangle_frame.set_index('Name')

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = "\n---- Right Angle Triangle Solve Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)


# Change frame to a string so that we can export it to file
right_angle_triangle_string = pandas.DataFrame.to_string(right_angle_triangle_frame)


# edit text below!! It needs to work if we have unsolved problem
if problems_sold == MAX_PROBLEMS:
    sales_status = "\n*** All the problems have been solve ***"
else:
    sales_status = "\n **** You have solve {} out of {} " \
                    "problem *****".format(problems_sold, MAX_PROBLEMS)


# list holding content to print / write to file
to_write = [heading, right_angle_triangle_string,
            sales_status
            ]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()


print("---- Problem Data ----")
print()

# output table with problem data
print(right_angle_triangle_frame)

print()
print("---- Problem Solve ----")


# Output number of problems sold
if problems_sold == MAX_PROBLEMS:
    print("Congratulations! You have complete all the problems ")
else:
    print("You have complete {} problem/s. There is {} problem/s "
          "remaining".format(problems_sold, MAX_PROBLEMS - problems_sold))
