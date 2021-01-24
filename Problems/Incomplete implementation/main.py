def startswith_capital_counter(names):
    counter = 0
    for name in names:
        letter = name[0]
        if letter.isupper():
            counter +=1
    return counter

#names_list = ["Bob", "tom", "Dick", "harry"]

#print(startswith_capital_counter(names_list))
