def recite(start_verse, end_verse):
    subjects = [
        "house that Jack built.",
        "malt",
        "rat",
        "cat",
        "dog",
        "cow with the crumpled horn",
        "maiden all forlorn",
        "man all tattered and torn",
        "priest all shaven and shorn",
        "rooster that crowed in the morn",
        "farmer sowing his corn",
        "horse and the hound and the horn",
    ]

    verbs = [
        "",
        "that lay in the ",
        "that ate the ",
        "that killed the ",
        "that worried the ",
        "that tossed the ",
        "that milked the ",
        "that kissed the ",
        "that married the ",
        "that woke the ",
        "that kept the ",
        "that belonged to the ",
    ]

    verses = []

    for i in range(start_verse - 1, end_verse):
        line = "This is the " + subjects[i]
        for j in range(i, 0, -1):
            line += " " + verbs[j] + subjects[j - 1]
        verses.append(line)

    return verses