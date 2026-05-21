count = 0

for num in range(1, 251):

    #  Convert number to string
    s = str(num)

    #  Count how many '5' digits inside it
    count += s.count("5")

print(count)