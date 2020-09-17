

def fibonacci():
    current, nxt = 0, 1
    while True:
        yield current
        current, nxt = nxt, current + nxt

def firstn(generator, n):
    gen = generator()
    for i in range(n):
        yield next(gen)

print(list(firstn(fibonacci, 10)))
