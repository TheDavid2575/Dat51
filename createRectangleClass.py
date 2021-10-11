# Working with classes to create a Rectangle!

class rectangle:
    'Creates a Rectangle'
    
    def setSize(self, width, height):
        'Sets width and height of rectangle'
        self.width = width * 1
        self.height = height * 1
    
    def perimeter(self):
        self.perimeter = (self.width * 2) + (self.height * 2)
        return self.perimeter
    
    def area(self):
        self.area = (self.width) * (self.height)
        return self.area

a = rectangle()
b = rectangle()

a.setSize(12, 2)
b.setSize(5,242)

print(a.perimeter())
print(b.area())
