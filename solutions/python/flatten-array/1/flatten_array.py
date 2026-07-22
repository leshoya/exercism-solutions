def flatten(iterable):
    res = []
    #go thru every element in the iterable list
    for item in iterable:
        if isinstance(item, list): #if an item is a list object
            res.extend(flatten(item)) #add every element of the item's list individually while skipping over None's 
        elif item is not None:
            res.append(item)
    return res