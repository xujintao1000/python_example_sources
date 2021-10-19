class CPU():
    pass

class Disk():
    pass

class Computer:
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

# 赋值 --
# 两个变量都指向同一个地址
# 也就是说一个边，另外一个也相应的会变

cpu1 = CPU()
cpu2 = cpu1
print(cpu1,id(cpu1))
print(cpu2, id(cpu2))

print("------")
disk = Disk()
computer1 = Computer(cpu1, disk)

# 浅拷贝

import copy

computer2 = copy.copy(computer1)
computer3 = Computer(cpu1, disk)
print(computer1, computer1.cpu, computer1.disk)
print(computer2, computer2.cpu, computer2.disk)
print(computer3, computer3.cpu, computer3.disk)

# 深拷贝

computer4 = copy.deepcopy(computer3)
print(computer3, computer3.cpu, computer3.disk)
print(computer4, computer4.cpu, computer4.disk)



