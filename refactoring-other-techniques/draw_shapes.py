# by Kami Bigdely
# Extract superclass.

class Shape:
    def __init__(self, x, y, name, visible):
      self.center_x = x
      self.center_y = y
      self.name = name
      self.visible = visible
      
    def display(self):
        if self.visible:
            print('drew the rectable.')
            
    def hide(self):
        self.visible = False
        
    def make_visible(self):
        self.visible = True
    
    def get_center(self):
        return self.x, self.y

class Circle(Shape):
    def __init__(self, x, y, r, name='circle', visible = True):
        super().__init__(x, y, name, visible)
        self.r = r

class Rectangle(Shape):
    def __init__(self, x, y, width, height, name='rectangle', visible = True):
        super().__init__(x, y, name, visible)
        self.width = width
        self.height = height

    def get_center(self):
        return self.x + self.width/2, \
               self.y + self.height/2 


if __name__ == "__main__":
    circle = Circle(0,0,10, False)
    circle.set_visible(True)
    circle.display()
    print('center point',circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display() # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point',rect.get_center())