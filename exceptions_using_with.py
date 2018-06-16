# 在try块中获取资源，然后在finally块中释放资源是一种常见的模式
# with语句使得这一过程可以以一种干净的姿态得以完成

with open("poem.txt") as f:
    for line in f:
        print(line, end='')

# 将关闭文件的操作交由with open来自动完成
