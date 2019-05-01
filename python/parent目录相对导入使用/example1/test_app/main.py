"""
可以尝试下不同的importlib导入方式：绝对导入与相对导入
绝对导入比较省心，相对导入要至少之前导入过一次，才可以正常导入
注释掉的sys这是暂时没有用，相对导入一定要加上引号作为字符串处理，不同级目录导入需要加上.或者..
"""

import importlib
import os
import sys

#print(sys.path[0])
#sys.path.append(sys.path[0])

# 绝对导入
#a = importlib.import_module("clazz.a")
#a.show()
# show A

import clazz
# 相对导入
b = importlib.import_module(".b", "clazz")
b.show()
# show B
