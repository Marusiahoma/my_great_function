def remove_palindroms(new_list):
    o = 0
    for i in new_list:
        p = i.split(" ")
        i = "".join(p)
        o += 1
        if i.lower() == i[::-1].lower():
            new_list.pop(o - 1)
    return new_list
