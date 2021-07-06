
def binary_search(testList, testItem):
    low = 0
    high = len(testList) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = testList[mid]
        if guess == testItem:
            found = mid
            return found
        elif guess > testItem:
            high = mid - 1
        else:
            low = mid + 1
    return None

