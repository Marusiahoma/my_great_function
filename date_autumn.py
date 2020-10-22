dates = ("11-27-2006", "12-01-2009", "08-31-2010", "11-28-2008")


def date_autumn(dates):
    la = []
    l = []
    lol = []
    ol = []
    for i in dates:
        p = i.split("-")
        if p[0] == "09" or p[0] == "10" or p[0] == "11":
            la.append(p)
    max = int(la[-1][2])
    for i in la:
        if max <= int(i[2]):
            l.append(i)
            max = int(i[2])
    data = int(i[-1][1])
    for i in l:
        if data <= int(i[1]):
            lol.append(i)
            data = int(i[1])
    for i in range(len(lol)):
        for j in range(len(lol[i])):
            ol.append(lol[i][j])
    return "-".join(ol)

print(date_autumn(dates))


