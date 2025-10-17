# multipule layer 乘法层

class Mullayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x * y
        return out
    
    def backword(self, dout):
        dx = dout * self.y 
        dy = dout * self.x

        return dx,dy
    
# add layer 加法层  
class AddLayer:
    def __init__(self):
        pass

    def forward(self,x,y):
        out = x + y
        return out

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx,dy    

