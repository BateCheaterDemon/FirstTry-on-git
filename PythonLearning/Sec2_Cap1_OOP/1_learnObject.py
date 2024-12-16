# 设计一个类
class Student: #驼峰命名法 PartTimeEmployee
    '''学生类
    属性 方法
    '''
    School="tsinghua" #类属性,在所有实例化之间共享值
    healthy="good"
    number=0
    def __init__(self,name=None,gender=None,nationality=None): #定义构造方法，只能有一个构造方法
        #(self是该方法第一个参数，必须存在，用于表示指向实例本身的引用，通过它可以访问这个类的属性和方法，其余参数放置后方)
        # Student.number+=1 
        # print("我是第%d名学生"%Student.number)

        # print("我是Student类，我的初始化特征") #验证构造方法运行成功
        # print(name,gender,nationality)
        # print(Student.School,Student.healthy)

        self.name=name #实例属性
        self.gender=gender
        self.nationality=nationality
        self.native_place=None
        self.age=None

        # print("我有以下实例属性") #访问实例属性,只能被类对象访问
        # print(self.name)
        # print(self.gender)

    def run(self,state = "not running"):# 默认设置
        print(state)

list1=[] #空列表
for i in range(4):
    list1.append(Student())

print("一共有%d个学生" %Student.number)

# print(list1[2].number)

Student.id="Student ID" #添加一个类属性
print(list1[2].id) #所有的已经有的类都被添加上了id这个新属性

# # 创建一个对象(创建实例)
Student1=Student("Zhangsan","男","China") 
Student2=Student("Lisi","男","China")
print(Student1.id)
Student.id=150 #类属性一改则全改
print(Student1.id)

print("查看类属性")
print(Student)

# # Student1.School="Peiking" #会被修改，但是不会直接修改类内，类内修改在init里
# # print(Student1.School)

# Student1.run("runnning") #调用实例方法
# Student1.run() #调用默认参数实例方法

# # print(Student1,Student2)
# # print(Student1)
