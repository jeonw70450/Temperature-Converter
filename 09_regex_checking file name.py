import re

has_errors= "yes"
while has_errors == "yes":
    print()
    filename = input("Enter a filename: ")
    has_errors = "No"

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(No spaces allowed)"

        else:
            problem = ("no {}'s allowed".format(letter))
        has_errors = "yes"


    if filename == "":
        problem = "Can't be blank"
        has_errors = "yes"


    if has_errors == "yes":
        print("Invalid Filename - {}".format(problem))

    else:
        print("You entered a filename")

