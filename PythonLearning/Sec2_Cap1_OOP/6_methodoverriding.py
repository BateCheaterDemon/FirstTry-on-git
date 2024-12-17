# 方法重写
# 父类/基类的方法如果不完全使用在子类/派生类，所以要重写方法

class Fruit:
    color="Green" #类属性
    def harvest(self,color): #此color相当于局部变量，与上边color无关
        print("水果的颜色：",color,"的！")
        print("水果已经收获")
        print("水果原来的颜色是：",Fruit.color) #输出类属性

class Apple(Fruit):
    color="红色"
    def __init__(self):
        print("我是苹果")

    def harvest(self, color): #此处相当于重写方法，调用的不再是父类，而是当前
        print("苹果的颜色：",color,"的！")
        print("苹果已经收获")
        print("苹果原来的颜色是：",Fruit.color) #输出类属性


class Orange(Fruit):
    color="橙色"
    def __init__(self):
        print("我是橘子")

    def harvest(self, color):
        print("橘子的颜色：",color,"的！")
        print("橘子已经收获")
        print("橘子原来的颜色是：",Fruit.color) #输出类属性

apple=Apple()
apple.harvest(apple.color) #调用基类的harvest方法

orange=Orange()
orange.harvest(orange.color) #调用基类的harvest方法
