


class Person(object):
    # def __init__(self, name, age):
    #     self.name = name
    #     slef.age = age

    def __new__(cls, *args, **kwargs):
        print("__new__ 被调用执行了。cls的id值为{0}".format(id(cls)))
        obj = super().__new__(cls)
        print("创建的对象的id为:{0}".format(id(obj)))
        return obj

    def __init__(self,name,age):
        print("__init__被调用了，self的id值为：{0}".format(id(self)))
        self.name = name
        self.age = age


print("object 这个类对象的id为:{0}".format(id(object)))
print("Person这个类对象的id为：{0}".format(id(Person)))

p1 = Person("张三", 20)
print("p1这个Person类的实力对象的id：{0}".format(id(p1)))

p2 = Person("张三", 20)
print("p2这个Person类的实力对象的id：{0}".format(id(p1)))