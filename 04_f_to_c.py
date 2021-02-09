# Conversion to Fahrenheit to Celsius
# Function takes input, does conversion and puts answer into list.


def to_c(deg_f):
    celsius = (deg_f - 32) * 5 / 9
    return celsius


# Main Routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = " {} degrees F is {} degrees C".format(item, answer)
    converted.append(ans_statement)

print(converted)
