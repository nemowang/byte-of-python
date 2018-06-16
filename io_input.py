# 输入与输出
# 做到忽略大小写，空格，标点符号
import string

def reverse(text):
    return text[::-1]

def is_palindrome(text):    #回文
    return text == reverse(text)


something = input("Enter text: ")
# 忽略大小写
something = something.lower()
# 忽略空格（将空格替换）
something = something.replace(' ','')
# 忽略标点符号
for char in string.punctuation:
    something = something.replace(char,'')
# 利用string.punctuation来表示中文标点符号是不行的


if is_palindrome(something):
    print("yse, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
    print(reverse(something))

# 我们使用切片功能翻转文本。
# 我们已经了解了我们可以通过使用 seq[a:b] 来从位置 a 开始到位置 b 结束来对序列进行切片。
# 我们同样可以提供第三个参数来确定切片的步长（Step）。
# 默认的步长为 1 ，它会返回一份连续的文本。
# 如果给定一个负数步长，如 -1 ，将返回翻转过的文本。
