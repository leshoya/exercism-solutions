def is_armstrong_number(number):
    numofdigits = len(str(abs(number)))
    sum = 0
    for num in str(number):
        sum += pow(int(num), numofdigits)
    return sum == number


    # rly keep track of variable types bc its harder in python than java
