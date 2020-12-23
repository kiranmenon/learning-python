#https://www.geeksforgeeks.org/multiple-inheritance-in-python

class A:
    def func(self):
        print("Im A")


class B(A):
    def func(self):
        print("Im B")

class C(A):
    def func(self):
        print("Im C")

class D(B, C):
    def func(self):
        print("Im D")

d = D()
d.func()
A.func(d)
B.func(d)
C.func(d)
