dates = ("11-27-2006", "12-01-2009", "08-31-2010", "11-28-2008")


def date_autumn(dates):
    la = []
    l = []
    max = 0
    for i in dates:
        p = i.split("-")
        if p[0] == "09" or p[0] == "10" or p[0] == "11":
            la.append(p)
    for i in la:




date_autumn(dates)