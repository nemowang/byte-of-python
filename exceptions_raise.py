# 抛出异常
# 通过raise语句来引发一次异常
# 用户定义的异常类必须直接或间接从属于Exception（异常）类的派生类

# encoding = UTF-8

class ShortInputException(Exception):
    '''一个由用户定义的异常类'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Enter something -->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)

except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was'+
          ' {0} long, expected at least {1}.')
          .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')
