def _private_1(name):
    return 'Hello,%s' % name

def _private_2(name):
    return 'Hi,%s' % name

def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)
    
# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，
# 这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。