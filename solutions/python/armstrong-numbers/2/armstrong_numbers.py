def is_armstrong_number(number):
    digits = str(number)
    length = len(digits)

    sum = 0
    for digit in digits:
        sum += int(digit) ** length
    return sum == number

    # rly keep track of variable types bc its harder in python than java
