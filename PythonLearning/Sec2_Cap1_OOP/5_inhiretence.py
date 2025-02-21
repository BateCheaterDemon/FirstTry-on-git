# 子类可继承父类

# 继承的基本语法
# class ClassName(baseclasslist): #存在多个基类可以用逗号分隔,如果不指定继承的类,则默认继承object
#     '''类的帮助信息（doc）'''
#     statement

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

    def cake(self):
        return "苹果派"

class Orange(Fruit):
    color="橙色"
    def __init__(self):
        print("我是橘子")

# apple=Apple()
# apple.harvest(apple.color) #调用基类的harvest方法

# orange=Orange()
# orange.harvest(orange.color) #调用基类的harvest方法

class BigApple(Apple):
    size="Big"
    def __init__(self):
        super().__init__()
        print("我是大苹果") #不会再逆上去初始化父类

bigapple=BigApple()
print(bigapple.cake())
# bigapple.harvest(bigapple.color)



