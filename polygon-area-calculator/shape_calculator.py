class Rectangle:
    def __init__(self, width, height):
        assert isinstance(width, int) and isinstance(height, int),\
            "Rectangle width and height must be integer numbers"
        self.__width = width
        self.__height = height

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def get_perimeter(self):
        return (2 * self.__width) + (2 * self.__height)

    def get_diagonal(self):
        return ((self.__width ** 2) + (self.__height ** 2)) ** 0.5

    def get_picture(self):
        if (int(self.__width) > 50) or (int(self.__height) > 50):
            return "Too big for picture."
        else:
            picture = ""
            for n in range(int(self.__height)):
                row = ("*" * int(self.__width)) + "\n"
                picture += row
            return picture

    def get_amount_inside(self, shape):
        if (self.__width >= shape.__width) and (self.__height >= shape.__height):
            inside_area = self.get_area()
            shape_area = shape.get_area()
            amount_inside = inside_area // shape_area
            return amount_inside
        else:
            return 0

    def __str__(self):
        return f"Rectangle(width={self.__width}, height={self.__height})"


class Square(Rectangle):
    def __init__(self, side):
        assert isinstance(side, int),\
            "Square side must be an integer number"
        super().__init__(side, side)

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

    def __str__(self):
        return f"Square(side={self._Rectangle__width})"


# Testing
if __name__ == "__main__":
    print("Testing Rectangle class".center(30, "*"))
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    print("Testing Square class".center(30, "*"))
    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())
    
    print("Testing get_amount_inside".center(30, "*"))
    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

    rect.set_height(3)
    rect.set_width(2)
    print(rect.get_amount_inside(sq))