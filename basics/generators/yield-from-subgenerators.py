def cities():
    return ["Berlin","Delhi","new York", "Bombay"]

def squares():
    for i in range(4):
        yield i ** 2

def cities_and_numbers():
    yield from cities()
    yield from squares()

l= [ cn for cn in cities_and_numbers()]
print(l)


