# 为类属性添加保护机制
# 之前有__foo方式可以设置私有属性，但是这样既不能修改也不能读取（实例名._类名__私有名还是可以的）
# 所以想要创建可以读取但是不能修改值的属性
# 使用装饰器@property

class TVshow:
    list_film=["战狼2","流浪地球","星际穿越","信条"] #列表
    def __init__(self,show):
        self.__show = show #构造了一个私有属性
        self.id=None
    
    @property
    def show(self):
        return self.__show #返回私有属性
    
    @show.setter #这样让它可以进行修改
    def show(self,value): #重载？
        if value in TVshow.list_film: #判断是否在列表中
            self.__show="您选择了《"+ value +"》稍后将播放" #修改返回值
        else:
            self.__show="您点播的电影不存在"

tvshow=TVshow("花儿与少年5")
print(tvshow.show)
#等同于使用
print(tvshow._TVshow__show) 
# 可以发现后边这个是灰色，证明它不知道后续这个是啥
# 即没有返回一个这样的类，但是它还是使用了，这部分可能需要我进一步找找

# 进行修改
# tvshow.show="《流浪地球》"
# print(tvshow.show)
# 访问私有，异常
# print(tvshow.__show)

# 使用装饰器可以实现为属性设置拦截器，即允许对属性进行修改，但是修改时需要遵守一定的规则
print(tvshow.list_film)
# 进行一个只允许在列表内电影的点播
tvselect=TVshow("魁拔")
print(tvselect.show)
tvselect.show="喜羊羊"
print(tvselect.show)
tvselect.show="流浪地球"
print(tvselect.show)

# tvselect.show("流浪地球") #用法是错误的，因为当前show已经变成一个属性而不是方法，无法使用方法赋值
# print(tvselect.show)

