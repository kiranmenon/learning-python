
def cycle(items):
    crntIndex = 0
    while len(items) != 0:
        yield items[crntIndex]
        crntIndex+=1
        if crntIndex >= len(items) :
            crntIndex = 0

countries = ["Germany", "Switzerland", "Austria"]
country_iterator = cycle(countries)
for i in range(7):
     print(next(country_iterator))
