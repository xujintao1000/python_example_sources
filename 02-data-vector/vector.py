


from math import hypot


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 如果没有__repr__, 当我们在控制台里打印一个向量的实例时，得到的
    # 字符串可能会是 <Vector object at 0x10e100070>
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)      # %r 代表对象

    def __abs__(self):
        return hypot(self.x, self.y)

    # bool(x) 的背后是调用 x.__bool__() 的结果；
    # 如果不存在 __bool__ 方法，那么 bool(x) 会尝试调用 x.__len__()
    # 若返回0，则 bool会返回False；否则 返回 True
    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    # 两个Vector 相加
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # 相乘
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


# Example
v1 = Vector(2, 4)
v2 = Vector(2, 1)

print("v1 = ", v1)
print("v1+v2 = ", v1+v2)

print("-- -- -- -- -- -- ")

v = Vector(3, 4)
print("abs(v * 3) = ", abs(v * 3))

