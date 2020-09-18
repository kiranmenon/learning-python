

def runningAvg():
    total = 0.0
    count = 0
    avg = None

    while True:
        newInt = yield avg
        count +=1
        total += newInt
        avg = total/count

ra = runningAvg()
next(ra)
for i in [7, 8, 11, 17, 10, 0, 8]:
    str = "value sent: {sent:d}, new avg: {avg:.2f}"
    print(str.format(sent=i, avg=ra.send(i)))





