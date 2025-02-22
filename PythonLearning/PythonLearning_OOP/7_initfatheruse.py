# 子类中调用基类的__init__()方法
# 在子类中定义__init__()方法后不会自动调用父类的__init__()方法
# 子类中不定义__init__()方法则自动调用父类的__init__()方法

class Fruit:
    def __init__(self,color="绿色"):
        Fruit.color=color #创建了一个类属性并赋值

    def harvest(self,color): #此color相当于局部变量，与上边color无关
        print("水果的颜色：",color,"的！")
        print("水果已经收获")
        print("水果原来的颜色是：",Fruit.color) #输出类属性

class Apple(Fruit):
    color="红色"
    def __init__(self):
        print("我是苹果")
        super().__init__() #调用基类的__init__()方法

    def harvest(self, color): #此处相当于重写方法，调用的不再是父类，而是当前
        print("苹果的颜色：",color,"的！")
        print("苹果已经收获")
        print("苹果原来的颜色是：",Fruit.color) #输出类属性


class Sapodilla(Fruit):
    def __init__(self,color):
        print("\n我是人参果")
        super().__init__(color)

    def harvest(self, color):
        print("人参果的颜色：",color,"的！")
        print("人参果已经收获")
        print("人参果原来的颜色是：",Fruit.color) #输出类属性

apple=Apple()
apple.harvest(apple.color) #调用基类的harvest方法

sapodilla=Sapodilla("白色")
sapodilla.harvest("金黄色带紫色条纹") #调用基类的harvest方法