import random

def trange (start, stop, step):
    current = list(start)
    while current < list(stop):
        min_borrow = hr_borrow = 0
        yield tuple(current)
        current[2] += step[2]
        if current[2] >= 60:
            current[2] -= 60
            min_borrow = 1
        current[1] += step[1] + min_borrow
        if current[1] >= 60:
            current[1] -= 60
            hr_borrow = 1
        current[0] += step[0] + hr_borrow
        if current[0] >=24:
            current[0] -= 24

f = open("time_and_temp.txt", 'w')
for r in trange( (6,0,0), (10,10,30), (0,1,30) ):
    f.write("%2d:%2d:%2d %2.1f\n" %(r[0], r[1], r[2], random.random()*100))



