# # GuessNumber
# import random
# Guess = int(input('Guess Number(1~100):'))
# Secret = random.randint(1,100)
#
# while True:
#     if Guess < Secret:
#         print('Wrong!Bigger!')
#     elif Guess > Secret:
#         print('Wrong!Smaller!')
#     else:
#         print('You smart ass!')
#         break
#     Guess = int(input())
#
# print('Game Over!')



# #using For
# for i in range(1,5):
#     print(list(range(i)))
# #range(a,b,c)输出从a到b-1,c为步长
# #list(range(5))输出[0,1,2,3,4]



# #Function
# def say_hello():
#     print('Hello world!')
#
# say_hello()



# #Function_param
# def max_number(a, b):
#     if a > b:
#         print(a,'is maximum.')
#     elif a < b:
#         print(b,'is maximum.')
#     else:
#         print(a,'is equal to',b)
#
# max_number(3,5)
# max_number(5,5)



# #Function_local
# x = 50
# def func(x):
#     x = 2
#     print('Change local x to',x)
#
# func(x)
# print('x is still',x)



# #Function_global 应避免在函数内使用定义于函数外的变量的值
# x = 50
# def func():
#     global x
#
#     print('x is',x)
#     x = 2
#     print('Change global x to',x)
#
# func()
# print('Value of x is',x)


#
# #Function_default 带默认值的参数(只有位于参数列表末尾的参数才能被赋予默认参数值)
# def say(message, times=1):
#     print(message * times)
#
# say('hello')
# say('world', 3)



# #Function_keyword 关键字参数_命名关键字，调用时可不按顺序
# def func(a, b=5, c=10):
#     print('a is',a, 'and b is', b, 'and c is', c)
#
# func(3)
# func(25, c=7)
# func(b=8, c=9, a=10)



# #Function_varargs 可变参数***********!!!!!!!
# def total(a=5, *numbers, **phonebook):
#     print('a', a)
#
#     #遍历元组中的所有项目
#     for single_item in numbers:
#         print('single_item', single_item)
#
#     #遍历字典中的所有项目
#     for first_part, second_part in phonebook.items():
#         print(first_part, second_part)
#
# print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))



# #Function_return
# def maximum(x, y):
#     if x > y:
#         return x
#     elif x < y:
#         return y
#     else:
#         return 'The numbers are equal.'
#
# print(maximum(2,3))
# print(maximum(3,3))



# #Function_docstring 文档字符串,可在help中显示出来
# def print_max(x, y):
#     '''Prints the maximum of two numbers.
#
#     The two values must be integers.'''
#     #if possible, make it integer
#     x = int(x)
#     y = int(y)
#
#     if x > y:
#         print(x, 'is maximum')
#     else:
#         print(y, 'is maximum')
#
# print_max(3, 5)
# print(print_max.__doc__)
#
# help(print_max)



# #Module_using_sys 使用标准库模块
# import sys
#
# print('The command line arguments are:')
# for i in sys.argv:
#     print(i)
#
# print('\n\nThe PYTHONPATH is', sys.path, '\n')



# #导入模块，将Python转换成中间形式的按字节码编译的文件，以.pyc为扩展名，
#
#
# from math import sqrt
# print('Square root of 16 is', sqrt(16))

# #Moduel_using_name
# if __name__ == '__main__':
#     print('This program is being run by itself')
# else:
#     print('I am being imported from another module')


# # mymodule_demo.py 要导入模块，则程序和模块要在相同的目录下
# import mymodule
# #from mymodule import say_hi, __version__
#
# mymodule.say_hi()
# print('Version', mymodule.__version__)
# help(mymodule)




# # ==================数据结构=====================
#
# # ========list 列表[]=========
# # ds_using_list
# shoplist = ['apple', 'mango', 'carrot', 'banana']
#
# print('I have', len(shoplist), 'items to purchase.')
#
# print('These items are:', end=' ')
# for item in shoplist:
#     print(item, end=' ')
#
# #append
# print('\nI also have to buy rice.')
# shoplist.append('rice')             #list.append此函数用来在list末尾添加元素
# print('My shop list is now:', shoplist)
#
# #sort
# print('I will sort my list now.')
# shoplist.sort()                     #sort排序
# print('Sorted shop list is', shoplist)
#
# # how to del from list
# print('The first item I will buy is', shoplist[0])
# olditem = shoplist[0]
# del shoplist[0]
# print('I bought the', olditem)
# print('My shop list is now', shoplist)



# # =========tuple 元组()========
# # ds_using_tuple
# zoo = ('python', 'tiger', 'elephant')
# print('Number of animals in the zoo is', len(zoo))
#
# new_zoo = 'monkey', 'camel', zoo
# print('Number of CAGES in the new zoo is', len(new_zoo))
# print('Number of animals in the new zoo is', len(new_zoo)-1+len(new_zoo[2]))
# print('All the animals in new zoo are', new_zoo)
# print('Animals brought from the old zoo is', new_zoo[2])
# print('Last animal brought from old zoo is', new_zoo[2][2])
#
# # 包含0或1个项目的元组,你必须在第一个（也是唯一一个）项目的后面加上一个逗号来指定它，singleton = (2, )



# 列表与元组的区别：
# 1.列表用[], 元组用()
# 2.列表内容可变，元组内容不可变，但可通过嵌套的形式添加
# 3.元组内可嵌套列表
# 4.在定义只有一个元素的元祖时加入"逗号"以免产生和数学运算的歧义
# 5.元组通常有不同的数据类型，而列表是相同类型的数据队列。元组表示的是结构，而列表表示的是顺序
# 6.列表不能当作字典的key， 而元组可以


# # =========dict 字典{:}==========
# # ds_using_dict
# #ab is address book
# ab = {
#     'Swaroop': 'swaroop@swaroopch.com',
#     'Larry': 'larry@wall.org',
#     'Matsumoto': 'matz@ruby-lang.org',
#     'Spammer': 'spammer@hotmail.com'
# }
#
# print("Swaroop's address is", ab['Swaroop'])
#
# #delete a key
# del ab['Spammer']
#
# print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
# #format前是“点”(.)
#
# #add a key
# ab['Guido'] = 'guido@python.org'
#
# if 'Guido' in ab:
#     print("\nGuido's address is", ab['Guido'])



# # =============序列（列表、元组、字符串都是序列Sequence的一种）=============
# # 序列的主要功能是资格测试（也就是in与not in表达式）和索引操作
# # 列表、元组和字符串（序列的三种形态），同样拥有切片运算符，它允许我们对序列切片（获得序列中的一部分）
# # ds_seq
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# name = 'LeonardoDiCaprio'
#
# # 索引或“下标”操作符
# print('Item 0 is', shoplist[0])
# print('Item 1 is', shoplist[1])
# print('Item 2 is', shoplist[2])
# print('Item 3 is', shoplist[3])
# print('Item -1 is', shoplist[-1])
# print('Item -2 is', shoplist[-2])
# # 索引为负值，表示倒序索引
# print('Character 0 is', name[0])
#
# #对list切片
# print('shoplist:',shoplist)
# print('Item 1 to 3 is', shoplist[1:3])
# print('Item 2 to end is', shoplist[2:])
# print('Item 1 to -1 is', shoplist[1:-1])
# print('Item start to end is', shoplist[:])
#
# #对字符串切片
# print('name:', name)
# print('characters 1 to 3 is', name[1:3])
# print('characters 2 to end is', name[2:])
# print('characters 1 to -1 is', name[1:-1])
# print('characters start to end is', name[:])
# print('字符串从开始到结束步长为2：', name[::2])


# # =================集合set================
# # 集合是简单对象的无序集合
# # 当集合中的项目存在与否比起次序更重要时，使用集合
# # 控制台运行以下命令
# #bri = set(['brazil', 'russia', 'india'])
# #'india' in bri
# #'usa' in bri



# # Reference引用
# #ds_reference
# print('Simple Assignment')
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# # mylist是指向同一对象的另一种名称
# mylist = shoplist
#
# # delete 0
# del shoplist[0]
#
# print('shoplist is', shoplist)
# print('mylist is', mylist)
# if 'apple' in mylist:
#     print('mylist is different with shoplist')
# else:
#     print('mylist is the same list with shoplist')
#
# print('Copy by making a full slice')
# # 通过生成一份完整的切片，制作一份列表的副本
# mylist = shoplist[:]
# del mylist[0]
#
# print('shoplist is', shoplist)
# print('mylist is', mylist)
# if shoplist[0] not in mylist:
#     print('通过切片制作副本，则mylist不再指向shoplist')


# # more about str
# name = 'LeonardoDicaprio'
# if name.startswith('Leo'):
#     print('Yes, the string starts with "Leo"')
#
# if 'a' in name:
#     print('Yes, it contains the string "a"')
#
# if name.find('cap')!=-1:
#     print('Yes, it contains the string "cap"')
#
# delimiter = '_*_'
# mylist = ['China', 'Russia', 'Brazil', 'India']
# print(delimiter.join(mylist))



# # 判断输入字符串是否为回文。允许存在大小写，空格，英文标点
# import string
#
# def reverse(text):
#     return text[::-1]
#
# def is_huiwen(text):
#     return text == reverse(text)
#
# something = input("Enter text:")
# # 忽略大小写
# something = something.lower()
# # 忽略空格
# something = something.replace(' ','')
# # 忽略英文标点符号
# for char in string.punctuation:
#     something = something.replace(char,'')
#
# if is_huiwen(something):
#     print('Yes, it is a palindrome.')
# else:
#     print('No, it is not a palindrome.')
#     print(reverse(something))
