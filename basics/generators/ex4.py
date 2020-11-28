def rtrange(start, stop, step):
    current = list(start)
    while current < list(stop):
        minutes_borrow = hr_borrow = 0
        new_start = yield tuple(current)
        if new_start != None:
            current = list(new_start)
            continue
        seconds = current[2] + step[2]
        if seconds > 60 :
            current[2] = seconds - 60
            minutes_borrow = 1
        else:
            current[2] = seconds
        minutes = current[1] + step[1] + minutes_borrow
        if minutes > 60 :
            current[1] = minutes - 60
            hr_borrow = 1
        else:
            current[1] = minutes
        hr = current[0] + step[0]+ hr_borrow
        if hr > 24 :
            current[0] = hr - 24
        else:
            current[0] = hr

timeGen = rtrange((6,0,0), (6, 20, 0), (0,1,30))
for _ in range(5):
    print(next(timeGen))

print(timeGen.send((0, 2, 0)))

for _ in range(25):
    print(next(timeGen))


