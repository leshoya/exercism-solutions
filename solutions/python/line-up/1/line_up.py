def line_up(name, number):
    ordinalnum = str(number)
    if number % 10 == 1 and number % 100 != 11:
        ordinalnum += "st"
    elif number % 10 == 2 and number % 100 != 12:
        ordinalnum += "nd"
    elif number % 10 == 3 and number % 100 != 13:
        ordinalnum += "rd"
    else:
        ordinalnum += "th"
    
    return f"{name}, you are the {ordinalnum} customer we serve today. Thank you!"
