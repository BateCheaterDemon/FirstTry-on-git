import unittest
from my_dict import Dict

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
# 对每一类测试都需要编写一个test_xxx()方法。
# 由于unittest.TestCase提供了很多内置的条件判断，
# 我们只需要调用这些方法就可以断言输出是否是我们所期望的。最常用的断言就是assertEqual()：

# self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等
# 另一种重要的断言就是期待抛出指定类型的Error，比如通过d['empty']访问不存在的key时，断言会抛出KeyError：
# with self.assertRaises(KeyError):
#     value = d['empty']

# 而通过d.empty访问不存在的key时，我们期待抛出AttributeError：
# with self.assertRaises(AttributeError):
#     value = d.empty

# 运行单元测试
# 一旦编写好单元测试，我们就可以运行单元测试。最简单的运行方式是在mydict_test.py的最后加上两行代码：
if __name__ == '__main__':
    unittest.main()

# 这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。
# 在开发阶段，很多时候，我们希望反复执行某一个测试方法，例如test_attr()，而不是每次都运行所有的测试方法，可以通过指定module.class.method来运行单个测试方法：
    '''
    /PythonLearning/Sec8_ErrorDebugTest/P3/mydict_test.py
    .....
    ----------------------------------------------------------------------
    Ran 5 tests in 0.001s

    OK
    '''

# 其中，module是文件名mydict_test（不含.py），class是测试类TestDict，method是指定的测试方法名test_attr。
# 如果希望执行test_attr()和test_attrerror()两个测试方法，我们可以传入-k参数，用attr来匹配：
'''
$ python -m unittest mydict_test -k attr -v
test_attr (mydict_test.TestDict.test_attr) ... ok
test_attrerror (mydict_test.TestDict.test_attrerror) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''
# 观察上述命令，-v参数能打印出具体执行的测试方法，-k attr参数筛选出了包含attr的测试方法。可见，单元测试的执行是十分灵活的。