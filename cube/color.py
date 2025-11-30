class Color:
    def __init__(self, red, green, blue):
        self.color = (red, green, blue)
        
    @property
    def red(self):
        return self.color[0]
    
    @property
    def green(self):
        return self.color[1]
    
    @property
    def blue(self):
        return self.color[2]

    def __mul__(self, other:float):
        return Color(other*self.red, other*self.green, other*self.blue)