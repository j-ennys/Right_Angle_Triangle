# checks that users enter a valid response (eg yes / no
# angle/degree or length or both) based on list of options
def string_checker(question, num_letters, valid_responses):

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (no integer valid)")


# main routine starts here
yes_no_list = ["yes", "no"]
method_list = ["angle", "degree", "length", "both"]

for case in range(0, 5):
    problem_method = string_checker("Choose a method (angle/degree or length or both) : ", 2, method_list)
    print("You chose", problem_method)