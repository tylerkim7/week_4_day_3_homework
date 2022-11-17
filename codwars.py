def unique_in_order(iterable):
    list = []
    for x in iterable:
        x in list[-1:] or list.append(x)
    return list


def spin_words(sentence):
    words = sentence.split(" ")
    wordss = []
    for word in words:
        if len(word) >= 5:
            word = word[::-1]
            wordss.append(word)
        else:
            wordss.append(word)
    return " ".join(wordss)


def likes(names):
    if len(names) == 0:
        return("no one likes this")
    elif len(names) == 1:
        return(names[0] + " likes this")
    elif len(names) == 2:
        return(names[0] + " and " + names[1] + " like this")
    elif len(names) == 3:
        return(names[0] + ", " + names[1] + " and " + names[2] + " like this")
    elif len(names) > 3:
        return f"{names[0]}, {names[1]} and {len(names)-2} others like this"