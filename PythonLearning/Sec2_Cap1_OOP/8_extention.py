# 用于记录我遇到的关于类的问题

# -> None 是一种类型提示，表示该方法不返回任何值，表明该函数方法返回值是None,没有也没影响
class Person:
    def __init__(self,name:str,age:int)->None:
        self.name=name
        self.age=age

    def greet(self)->None:
        print(f"Hello!my name is {self.name},I am {self.age} years old!")

person=Person("Lisi",19)
person.greet()

