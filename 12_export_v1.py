import pandas
from datetime import date

# lists to hold ticket details
all_names = ["a", "b", "c", "d", "e", "f"]

right_angle_triangle_dict = {
    "Name": all_names,

}
# create frame
right_angle_triangle_frame = pandas.DataFrame(right_angle_triangle_dict)




# set index at end (before printing)
right_angle_triangle_frame = right_angle_triangle_frame.set_index('Name')

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

heading = "---- Right angle Triangle solver Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)


# Change frame to a string so that we can export it to file
right_angle_triangle_string = pandas.DataFrame.to_string(right_angle_triangle_frame)


# edit text below!! It needs to work if we have unsold tickets
sales_status = "\n*** All the problems have been solve ***"


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
