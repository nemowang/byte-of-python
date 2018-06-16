# 类变量与对象变量：

# 类变量是共享的，他们可以被属于该类的所有实例访问，当任何一个对象对类变量做出改变时，发生的变动在其它所有实例中都会得到体现。
# 对象变量由类的每一个独立的对象或实例所拥有。
# oop_objvar.py
# coding = UTF-8
from mymodule import say_hi


# 所有类成员（包括数据成员）都是公开的，所有的方法都是虚拟的
# 如果在数据成员名字中使用双下划线为前缀，Python会使用名称调整使其成为私有变量



class Robot:
    """表示有一个带有名字的机器人。"""
    # 一个类标量，用来计数机器人的数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name
        print("(Initializing {})".format(self.name))

        #机器人增加人口数量
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} is the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """来自机器人的诚挚问候
        没问题，你做得到。"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod    #类方法  @classmethod装饰器等价于调用：how_many = classmethod(how_many)
    def how_many(cls):
        """打印出当前的人口数量"""
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destory them.")
droid1.die()
droid2.die()

Robot.how_many()

help(Robot.say_hi)
