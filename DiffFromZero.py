# Write the function implementation here
# 1234 = 4
# is 4 -> 3 -> 2 -> 1 == 0?


# 1203 = 3

def ndigitsnotzero(value):
    count = 0
    while value > 0:
        remainder = value % 10
        value = value // 10
        if remainder != 0:
            count = count + 1
    return count


# Main Program (DO NOT MODIFY THIS SECTION OF THE CODE)

number = int(input("Enter the number: "))
print("The number of digits different than zero is",ndigitsnotzero(number))