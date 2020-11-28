
def Dynamic_step_counter(firstVal=1, step=1):
    counter= firstVal
    while True:
        newStepSize= yield(counter)
        if newStepSize is None:
            counter += step
        else:
            counter += newStepSize
            step = newStepSize

counter = Dynamic_step_counter()

for i in range(10):
    print(next(counter), end=", ")

print("step size now changed.")
print(counter.send(5))
for i in range(20):
    print(next(counter), end=", ")

