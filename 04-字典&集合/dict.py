# 第三章 字典和集合

#----- Dict 创建  构造方法 -----#
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)

# 3.2　字典推导
# 根据已知字典分裂成两个数据列表
DIAL_CODES = [
                 (86, 'China'),
                 (91, 'India'),
                 (1, 'United States'),
                 (62, 'Indonesia'),
                 (55, 'Brazil'),
                 (92, 'Pakistan'),
                 (880, 'Bangladesh'),
                 (234, 'Nigeria'),
                 (7, 'Russia'),
                 (81, 'Japan')
]
country_code = {country: code for code, country in DIAL_CODES} ➋
print(country_code)
# {'China': 86, 'India': 91, 'Bangladesh': 880, 'United States': 1,
# 'Pakistan': 92, 'Japan': 81, 'Russia': 7, 'Brazil': 55, 'Nigeria':
# 234, 'Indonesia': 62}

pritn({code: country.upper() for country, code in country_code.items() ➌if code < 66})
# {1: 'UNITED STATES', 55: 'BRAZIL', 62: 'INDONESIA', 7: 'RUSSIA'}


# 3.3　常见的映射方法
# dict、collections.defaultdict和
# collections.OrderedDict





