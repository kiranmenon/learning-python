class printHaiDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        return "Hai " + self.function()

class printHelloDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        return "Hello " + self.function()



@printHaiDecorator
@printHelloDecorator
def myName():
    return "Kiran"

if __name__=="__main__":
    print(myName())

