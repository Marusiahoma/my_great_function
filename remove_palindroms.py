def remove_palindroms(new_list):
    for i in new_list:
        if i.lower() == i[::-1].lower():
            new_list.remove(i)
    return new_list
