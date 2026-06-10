def response(hey_bob):
    if hey_bob.strip() == "" or hey_bob is None:
        return "Fine. Be that way!" 

    if hey_bob.isupper() and "?" in hey_bob:
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!" 
    elif hey_bob.strip().endswith("?"):
        return "Sure."



    return "Whatever."
