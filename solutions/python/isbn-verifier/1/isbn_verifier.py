def is_valid(isbn):
    s = isbn.replace("-", "")
    if len(s) != 10:
        return False

    try:
        values = [10 if c == "X" and i == 9 else int(c) for i, c in enumerate(s)]
    except ValueError:
        return False

    if "X" in s[:-1]:
        return False

    return sum(v * (10 - i) for i, v in enumerate(values)) % 11 == 0