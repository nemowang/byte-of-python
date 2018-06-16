# 继承
# 基类和派生类/超类和子类

# coding = UTF-8

class SchoolMember:
    '''代表任何学校里的成员。'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember:{})'.format(self.name))

    def tell(self):
        '''tell me about detail'''
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


class Teacher:
    '''代表一位老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{:d}"'.format(self.salary))


class Student:
    '''代表一位学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


# 实例化
t = Teacher('Mrs.Xiang', 21, 12000)
s = Student('NemoWang', 22, 87)

print()

members = [t, s]
for member in members:
    member.tell()
