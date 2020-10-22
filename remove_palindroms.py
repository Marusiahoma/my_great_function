def remove_palindroms(new):
    for i in new:
        if i.lower() == i[::-1].lower():
            new.remove(i)
    return new
