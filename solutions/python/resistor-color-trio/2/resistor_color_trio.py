def label(colors):
    values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    number = (10 * values[colors[0]] + values[colors[1]]) * 10 ** values[colors[2]]
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    unit = 0
    while number >= 1000 and unit < len(units) -1:
        number//= 1000
        unit += 1
    return f"{number} {units[unit]}"
