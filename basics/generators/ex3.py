
def trange(start, stop, step):
    current = list(start)
    while current < list(stop):
        yield tuple(current)
        current[2] += step[2]
        min_borrow = 0
        hr_borrow = 0
        if current[2] >=  60:
            current[2] -= 60
            min_borrow = 1
        current[1] += step[1] + min_borrow
        if current[1] >= 60:
            current[1] -= 60
            hr_borrow = 1
        current[0] += step[0] + hr_borrow
        if current[0] >= 24:
            current[0] -= 24

for time in trange((10, 10, 10), (19, 53, 15), (1, 24, 12) ):
    print(time)

