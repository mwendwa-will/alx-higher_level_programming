#!/usr/bin/python3

class Bass:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def showtable(self):
        rect = []
        for i in range(self.height):
            for j in range(self.width):
                rect.append("#")
            rect.append("\n")
        return ''.join(rect)

x = Bass(5, 5)
print(x.showtable())