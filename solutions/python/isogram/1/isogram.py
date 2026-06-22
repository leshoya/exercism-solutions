def is_isogram(string):
    s = [c for c in string.lower() if c.isalpha()]
    return len(s) == len(set(s))