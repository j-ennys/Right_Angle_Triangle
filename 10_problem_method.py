import math
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
