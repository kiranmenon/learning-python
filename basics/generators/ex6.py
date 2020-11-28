import random

def random_ones_and_zeroes():
    prob1 = 50
    prob2 = 100 - prob1
    while True:
        choice = random.choices(population=[0,1], weights=[prob2, prob1])
        prob1 = yield choice
        if prob1 == None:
            prob1 = 50
        prob2 = 100-prob1

onesAndZeroes = random_ones_and_zeroes()

for _ in range(10):
    print(next(onesAndZeroes))

print(onesAndZeroes.send(80))
for _ in range(10):
    print(next(onesAndZeroes))
