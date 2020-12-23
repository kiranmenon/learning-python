#https://www.geeksforgeeks.org/method-resolution-order-in-python-inheritance/

class A:
    def whoAmI(self):
        print("Im A")

class B(A):
    def whoAmI(self):
        print("Im B")

class C(A):
    def whoAmI(self):
        print("Im C")

class D(C,B):
    pass

d = D()
d.whoAmI()

