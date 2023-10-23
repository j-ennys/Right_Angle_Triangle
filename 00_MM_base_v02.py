import pandas
from datetime import date
import math

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

def digit_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            elif response == "":
                print("Sory, this can't be blank. Please try again.")
            else:
                return response

        except ValueError:
            print(error)


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


# Lists to hold problem details
all_names = []

# Dictionary used to create frame ie: column_name:list
right_angle_triangle_dict = {
    "Name": all_names,

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


    problems_sold += 1


    # right angle triangle default 90 degree
    def right_angle_triangle_calculator():
        print("Right-Angled Triangle Calculator")
        print("an. Calculate Angle")
        print("le. Calculate Length")

        choice = input("Enter your choice (an/le): ")

        if choice == 'an':
            opposite = digit_check("Enter the length of the opposite side: ", "This only valid digit\n", float)
            adjacent = digit_check("Enter the length of the adjacent side: ", "This only valid digit\n", float)

            angle_rad = math.atan2(opposite, adjacent)
            angle_deg = math.degrees(angle_rad)

            print(f"The angle is {angle_deg:.2f} degrees")
        elif choice == 'le':
            known_side = digit_check("Enter the length of the known side: ", "This only valid digit\n", float)
            angle_deg = digit_check("Enter the known angle in degrees: ", "This only valid digit\n", float)

            angle_rad = math.radians(angle_deg)
            unknown_side = known_side / math.tan(angle_rad)

            print(f"The length of the unknown side is {unknown_side:.2f}")
        else:
            print("Invalid, digit or blank not allowed. Please try again.")


    #  general triangle
    def general_triangle_calculator():
        print("General Triangle Calculator")
        print("an. Calculate Angle")
        print("le. Calculate Length")

        choice = input("Enter your choice (an/le): ")

        if choice == 'an':
            side_a = digit_check("Enter the length of side opposite: ", "This only valid digit\n", float)
            side_b = digit_check("Enter the length of side adjacent: ", "This only valid digit\n", float)
            side_c = digit_check("Enter the length of side hypotenuse: ", "This only valid digit\n", float)

            angle_A_rad = math.acos((side_b ** 2 + side_c ** 2 - side_a ** 2) / (2 * side_b * side_c))
            angle_B_rad = math.acos((side_a ** 2 + side_c ** 2 - side_b ** 2) / (2 * side_a * side_c))
            angle_C_rad = math.acos((side_a ** 2 + side_b ** 2 - side_c ** 2) / (2 * side_a * side_b))

            angle_A_deg = math.degrees(angle_A_rad)
            angle_B_deg = math.degrees(angle_B_rad)
            angle_C_deg = math.degrees(angle_C_rad)

            print(f"Angle A is {angle_A_deg:.2f} degrees.")
            print(f"Angle B is {angle_B_deg:.2f} degrees.")
            print(f"Angle C is {angle_C_deg:.2f} degrees.")
        elif choice == 'le':
            print("Choose which length you want to calculate:")
            print("op. Calculate side opposite")
            print("ad. Calculate side adjacent")
            print("hy. Calculate side hypotenuse")

            side_choice = input("Enter your choice (op/ad/hy): ")

            if side_choice == 'op':
                angle_A_deg = digit_check("Enter angle A in degrees: ", "This only valid digit\n", float)
                side_b = digit_check("Enter the length of side adjacent: ", "This only valid digit\n", float)
                side_c = digit_check("Enter the length of side hypotenuse: ", "This only valid digit\n", float)

                angle_A_rad = math.radians(angle_A_deg)
                side_a = math.sqrt(side_b ** 2 + side_c ** 2 - 2 * side_b * side_c * math.cos(angle_A_rad))

                print(f"The length of side opposite is {side_a:.2f}.")
            elif side_choice == 'ad':
                angle_B_deg = digit_check("Enter angle B in degrees: ", "This only valid digit\n", float)
                side_a = digit_check("Enter the length of side opposite: ", "This only valid digit\n", float)
                side_c = digit_check("Enter the length of side hypotenuse: ", "This only valid digit\n", float)

                angle_B_rad = math.radians(angle_B_deg)
                side_b = math.sqrt(side_a ** 2 + side_c ** 2 - 2 * side_a * side_c * math.cos(angle_B_rad))

                print(f"The length of side adjacent is {side_b:.2f}.")
            elif side_choice == 'hy':
                angle_C_deg = digit_check("Enter angle C in degrees: ", "This only valid digit\n", float)
                side_a = digit_check("Enter the length of side opposite: ", "This only valid digit\n", float)
                side_b = digit_check("Enter the length of side adjacent: ", "This only valid digit\n", float)

                angle_C_rad = math.radians(angle_C_deg)
                side_c = math.sqrt(side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * math.cos(angle_C_rad))

                print(f"The length of side c is {side_c:.2f}.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")


    #  Loop
    while True:
        print("Triangle Calculator")
        print("rt. Right-Angled Triangle")
        print("gt. General Triangle")
        print("qu. Quit")

        option = input("What do you want to do? (rt/gt/qu): ")

        if option == 'rt':
            right_angle_triangle_calculator()
        elif option == 'gt':
            general_triangle_calculator()
        elif option == 'qu':
            print("Thank you for using this program! Do you want to continue and solve more unknown value/s?")
            break
        else:
            print("Invalid option. Please choose again.")

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
