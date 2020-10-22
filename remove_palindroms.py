def remove_palindroms(news):
    for i in news:
        if i.lower() == i[::-1].lower():
            news.remove(i)
    return news
