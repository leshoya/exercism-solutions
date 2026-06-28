def label(colors):
    values = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
    }
    n = (10 * values[colors[0]] + values[colors[1]]) * 10 ** values[colors[2]]
    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    i = 0
    while n>= 1000 and i < len(units) -1:
        n//= 1000
        i += 1
    return f"{n} {units[i]}"
