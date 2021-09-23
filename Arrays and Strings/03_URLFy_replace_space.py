input_string = input()
final_string = ""

for i in range(len(input_string)):
    if input_string[i] == ' ':
        final_string +='%20'
    else:
        final_string += input_string[i]

print(final_string)
