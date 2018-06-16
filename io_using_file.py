# 文件

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# 使用内置的open函数并制定文件名，以及打开模式
# 打开模式可以使阅读('r')，写入('w')和追加('a')
# 还可以选择通过文本('t')或二进制('b')来读取写入或追加文本
# 打开文件以编辑('w'riting)
f = open('poem.txt', 'w')
# 向文件中编写文本
f.write(poem)
# 关闭文件
f.close()

# 如果没有特别指定，
# 将假定启用默认的阅读('r'ead)模式
f = open('poem.txt')
while True:
    line = f.readline()     #读取文件的一行
    # 零长度指示 EOF
    if len(line) == 0:
        break
    # 每行('line')的末尾
    # 都已经有了换行符
    # 因为它是从一个文件中进行读取的
    print(line, end='')
# 关闭文件
f.close()
