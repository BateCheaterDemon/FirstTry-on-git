import unittest
from my_dict import Dict

class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')
        self.d = Dict(a=1, b=2)

    def tearDown(self):
        print('tearDown...')

    def test_attr(self):
        self.assertEqual(self.d.a, 1)
        self.assertEqual(self.d['a'], 1)

# unittest 框架会自动发现并运行以 test 开头的方法。
# 如果你的测试方法没有以 test 开头，它们不会被运行。
# 例如，test_attr 是一个有效的测试方法，而 test_attrerror 也是有效的，但 attr 或 attr_error 则不会被运行。

if __name__ == '__main__':
    unittest.main()
