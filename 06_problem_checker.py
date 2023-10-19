# functions go here
def angle_length(question):

    while True:
        response = input(question).lower()

        if response == "angle" or response == "an":
            return "angle/degree"

        if response == "degree" or response == "de":
            return "angle/degree"

        if response == "length" or response == "le":
            return "length"

        elif response == "both" or response == "bo":
            return "both"

        else:
            print("Please enter method, angle or length (an/le), no integer valid")


# main routine goes here
while True:
    problem_method = angle_length("What method do you want? Angle/Degree or Length or both : ")

    print("You choose", problem_method)

    print("program continues...")
    print()