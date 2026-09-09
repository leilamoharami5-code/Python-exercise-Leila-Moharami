#daryaft yek reshte
#hazf -> horof tekrary


a = input('enter string : ')

mainlist = []

for word in a.split():
    newlist = []

    for i in word:
        if i not in newlist:
            newlist.append(i)

    mainlist.append("".join(newlist))

end = " ".join(mainlist)

print(end)
