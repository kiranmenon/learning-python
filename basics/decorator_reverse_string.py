
def reversedString(function):
    def wrapper():
        reversedString = "".join(reversed(function()))
        return reversedString

    return wrapper

@reversedString
def helloWorld():
    return "hello-world"

if __name__=="__main__":
    print(helloWorld())

