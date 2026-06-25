def rotate(text, key):
    res = []
    for c in text:
        if c.isalpha():
            if c.isupper():
                shifted = (ord(c) - ord('A') + key) % 26 + ord('A')
            else:
                shifted = (ord(c) - ord('a') + key) % 26 + ord('a')
            res.append(chr(shifted))
        else:
            res.append(c)

    return ''.join(res)
