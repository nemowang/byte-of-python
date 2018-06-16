import os
import time

# 1.需要备份的文件与目录将被指定在一个列表中。
#   例如在Windows下：
source = ['"E:\\Code Studying\\Python\\BackupSource"']
#   在这里要注意必须在字符串中用双引号，用以括起其中包含空格的名称。

# 2.备份文件必须存储在一个主备份目录中
#   例如在Windows下：
target_dir = "E:\\Code Studying\\Python\\Backup"

# 如果存放备份文件的目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)    # 创建目录

# 3.备份文件将打包成zip文件。
# 4.zip压缩文件的文件名由当前日期与时间构成。
today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'

# 如果子目录尚不存在则创建一个
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5.使用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))


# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
