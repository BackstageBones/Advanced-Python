from math import sin, cos


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


if __name__ == '__main__':
    p = Point.new_cartesian_point(1, 2)
    d = Point.new_polar_point(1, 2)
    print(p, d)
