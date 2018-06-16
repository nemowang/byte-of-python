# Finally
# 当然，try...except也可以结合finally使用。
# 则将finally放在最后，finally语句块的内容通常是做一些后事的处理，比如资源释放
# 并且finally语句块是无论如何都要执行的，
# 即使在前面的try和except语句块中出现了return，
# 都现将finally语句执行完再去执行前面的return语句。

import sys
import time

f = None
try :
    f = open('poem.txt')
    # 我们常用的阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 确保它能运行一段时间
        # 每打印一行后插入两秒休眠
        time.sleep(2)
except IOError:
    print('Could not find file poem.exe')
except KeyboardInterrupt:
    print('!!You cancelled the reading from the file.')
finally:
    if f:
        f.close()
    print('(Cleaning up: Closed the file.)')
