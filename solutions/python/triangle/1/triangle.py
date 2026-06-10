def equilateral(sides):
    if 0 not in sides:
        if sides[0] == sides[1]:
            return sides[1] == sides[2]
    return False


def isosceles(sides):
    if sides[0] == sides[1] and (sides[0] + sides[1] >= sides[2]):
        return True
    if sides[0] == sides[2] and (sides[0] + sides[2] >= sides[1]):
        return True
    if sides[1] == sides[2] and (sides[1]*2 >= sides[0]):
        return True
    return False

def scalene(sides):
    max_n = max(sides)
    if sides[0] not in sides[1:]:
        if sides[1] != sides[2] and (sides[1] + sides[2] >= max_n):
            return True
    return False
