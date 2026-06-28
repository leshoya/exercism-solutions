def commands(binary_str):
    code = []
    actions = ["wink", "double blink", "close your eyes", "jump"]
    for i, number in enumerate(reversed(binary_str)):
        if i == 4 and number == "1":
            code.reverse()
        if number == "1" and i < 4:
            code.append(actions[i])
        
    return code