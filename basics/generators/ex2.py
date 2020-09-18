


def frange(*args):
    startVal = 0
    endVal = 0
    stepSize = 1

    if len(args) == 1:
        endVal = args[0]
    elif len(args) == 2:
        startVal = args[0]
        endVal = args[1]
    elif len(args) == 3:
        startVal, endVal, stepSize = args

    value = startVal
    while value < endVal:
        yield value
        value += stepSize

print("0 to 4.5:")
for f in frange(4.5):
    print(f)

print("0.5 to 5 : ")
for f in frange(0.5, 5):
    print(f)

print("1 to 5 with step 0.5: ")
for f in frange(1, 5, 0.5):
    print(f)
