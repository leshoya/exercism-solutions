def value(colors):
    key = {"black": 0,
           "brown": 1,
           "red": 2,
           "orange": 3,
           "yellow": 4,
           "green": 5,
           "blue": 6,
           "violet": 7,
           "grey": 8,
           "white": 9}
    res = 0
    for i, color in enumerate(colors):
        if i < 2:
            res = res*10 + key[color]

    return res
        
