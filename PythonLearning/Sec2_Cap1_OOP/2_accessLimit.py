#之前的类方法没有访问限制，所以如何实现访问权限限制？
#方法：可以在属性或者类前边写为 
# _foo(单下划线，表示protected类型，只允许类本身和子类可以访问) 
# __foo (private表示私有类型的成员，只允许定义类的本身可以访问，也可以类的实例名._类名__foo来访问) 
# __foo__(此为系统类，类似__init__()表示特殊的方法)


# _foo(单下划线，表示protected类型，只允许类本身和方法访问) 
class Swan:
    '''天鹅类'''
    _neck_swan="its too Long" #受保护类的属性
    __leg_swan="two leg"
    def __init__(self):
        print("__init__()：",Swan._neck_swan) #访问保护类型的属性
        print("__init__()：",Swan.__leg_swan) #访问private类型的属性

swan=Swan() #创建Swan类的实例（对象）
print("直接访问:",swan._neck_swan) #通过实例名访问受保护类型
print("类访问：",Swan._neck_swan ) #直接查询类

# __foo (private表示私有类型的成员，只允许定义类的本身可以访问，也可以类的实例名._类名__foo来访问) 
# print("直接访问:",swan.__leg_swan) #通过实例名访问受保护类型,访问失败,抛出异常
print("直接访问:",swan._Swan__leg_swan) #通过实例名访问受私有类型

#无法访问私有
# print(swan.__leg_swan)