class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"In this point x = {self.x} and y = {self.y}"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False



def main():
    p1 = Point(3, 6)
    p2 = Point(3, 6)
    if p1 == p2:
        print("Same")
    else:
        print("Not same")

    if p1 == 2:
        print("hi")



if __name__ == '__main__':
    main()
