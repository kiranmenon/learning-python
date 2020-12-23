class Square(Object):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

class Cube(Square):
    def area(self):
        return super().area() * 6
    def volume(self):
        return super().area() * self.side

class SquarePrism(Square):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def face_area(self):
        print("face_area: Im in SquarePrism")
        base_area = super().area()
        lateral_area = self.side * self.height
        return base_area, lateral_area

    def area(self):
        base_area, lateral_area = face_area()
        return 2 * base_area + 4 * lareral_area

class Cube2(SquarePrism):
    def __init__(self, side):
        super().__init__(side, side)

    def face_area(self):
        print("face_area: Im in Cube2")
        return super(SquarePrism, self).area()

    def area(self):
        return super().area()
