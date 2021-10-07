# 列表推导 list comprehension -- listcomps
# 生成器表达式 generator expression -- genexps

import os

# 方法-1
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)
# [36, 162, 163, 165, 8364, 164]

# 方法2
codes2 = [ord(symbol) for symbol in symbols]
print(codes2)

print("--- --- ---")


beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

print("--- --- ---")

lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates # 元组拆包
print("latitude = %s, longitude=%s" % (latitude, longitude))

print("--- --- ---")

print("divmod(20, 8) = ", divmod(20, 8))
t = (20, 8)

# 还可以用 * 运算符把一个可迭代对象拆开作为函数的参数：
quotient, remainder = divmod(*t)
print("quotient = %s, remainder = %s" % (quotient, remainder))

# 路径操作


# print(os.path)
# print("%s" % str(os.path))
_, filename = os.path.split(('/home/luciano/.ssh/idrsa.pub'))
print("%s" % filename)


print("--- --- ---")

a, b, *rest = range(5)
print(a, b, rest)

*head, b, c, d = range(6)
print(head, b, c, d)

print("--- --- ---")
# 文字展示
print("--- 文字展示 ---")

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   # <1>
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


print('{:20} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:20} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # <2>
    if longitude <= 0:  # <3>
        print(fmt.format(name, latitude, longitude))

print("--- --- ---")
# 具名元祖
# collections.namedtuple()

from collections import namedtuple
City = namedtuple("City", "name country population coordinates")
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print("Tokyo: ", tokyo)
print("Tokyo's population: ", tokyo.population)

print("--- --- ---")


invoice = """
... 0.....6................................40........52...55........
1909  Pimoroni PiBrella                        $17.50   3    $52.50
1489  6mm Tactile Switch x20                   $4.95    2    $9.90
1510 Panavise Jr. - PV-201                     $28.00   1    $28.00
1601 PiTFT Mini Kit 320x240                    $34.95   1    $34.95
"""

# 解切片（slice）对象
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])

print("--- --- ---")
print("2.4.3　多维切片和省略")
# 2.4.3　多维切片和省略
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
l[2:5] = [100]
print(l)


# Chapter 2.5
