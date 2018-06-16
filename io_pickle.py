# 标准模块Pickle
# 通过它可以将任何纯Python对象存储到一个文件中
# 并在稍后将其取回
# 叫作持久地(Persistently)存储对象

import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of things to buy
shoplist = ['banana', 'apple', 'orange', 'mango']

# Write to the file
# 以写入二进制模式打开文件
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)    #dump卸载（存储）数据
f.close()

# Destroy the shoplist variable
del shoplist

# Read back from the storage
f = open(shoplistfile, 'rb')
# Load the object from the file
storedlist = pickle.load(f) #load装载（加载）数据
print(storedlist)
