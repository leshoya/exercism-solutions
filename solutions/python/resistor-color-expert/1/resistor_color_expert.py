def resistor_label(colors):
    values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    tolerance = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
    }
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    def labeler(num):
        unit = 0
        while num >= 1000 and unit < len(units) - 1:
            num /=1000
            unit += 1
        if num.is_integer():
            num = int(num)
        return f"{num} {units[unit]}"
        
    if len(colors) < 5:
        if len(colors) == 1: return "0 ohms" 
        number = (10 * values[colors[0]] + values[colors[1]]) * 10 ** values[colors[2]]
        return labeler(number) + f" ±{tolerance[colors[3]]}%"
    number = (100 * values[colors[0]] + 10*values[colors[1]] + values[colors[2]]) * 10 **values[colors[3]]
    return labeler(number) + f" ±{tolerance[colors[4]]}%"
    
