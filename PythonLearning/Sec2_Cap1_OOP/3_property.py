# property(属性)！=类属性和实例属性
# property属性将在访问计算算后所得值

# 创建用于计算的属性 @property 装饰器
'''
@property
def methodname(self):
    block #该方法体一般包括return语句返回结果
'''

class Rect:
    def __init__(self,width,height): #构造方法
        self.width=width
        self.height=height

    @property #使用装饰器把方法转为属性
    def area(self):
        return self.width*self.height
    
rect = Rect(800,600) #创建类的实例
print(f"面积为:{rect.area}") #这样的area就从方法变成了Rect的一个类属性

rect.area=100
print(f"面积为:{rect.area}") #抛出异常，表示不能被赋值

    
    
