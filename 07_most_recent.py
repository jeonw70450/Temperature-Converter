# Compute data from the user and store it into a list then display the most recent activities.


all_calculations = []

# Get five items of Data
get_item = ""
while get_item != "xxx":
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)


print()

if len(all_calculations) == 0:
    print ("The list is empty.")

else:

    # Show that everything made it onto the list...
    print()
    print("*** The Full List ***")
    print(all_calculations)


    #Print items starting from the end
    if len(all_calculations) >=3:
        print("*** Most recent 3 ***")
        for item in range(0,3):
            print(all_calculations[len(all_calculations) - item - 1])


    else:
        print("*** Items from Newest to Oldest ***")
        for item in all_calculations:
            print(all_calculations[len(all_calculations) - all_calculations.index(item)])
