class A:
    def func1(self):
        self.overridedFunc()

    def overridedFunc(self):
        print("Im in class A")

class B(A):
    def overridedFunc(self):
        print("Im in class B")


b = B()
b.func1()

