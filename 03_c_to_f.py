# Conversion to Celsius to Fahrenheit
# Function takes input, does conversion and puts answer into list.


def to_f(deg_c):
    fahrenheit = (deg_c * 9 / 5) + 32
    return fahrenheit


# Main Routine
temperatures = [0, 40, 100]
converted = []

for item in temperatures:
    answer = to_f(item)
    ans_statement = " {} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)

print(converted)
