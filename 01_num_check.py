def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine goes here
get_int = num_check("Value of angle A : ",
                    "Please enter digit more than 0 & integer dose not valid\n",
                    int)
get_float = num_check("Value of angle B : ",
                    "Please enter digit more than 0 & integer dose not valid\n",
                    float)
