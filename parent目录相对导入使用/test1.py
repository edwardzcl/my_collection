# 方法二：
# 好像同一个文件，使用两种不同方式import两次，也只会执行一次里面的内容，看不出效果来，为此，我新建了test1.py
from test.sub2 import sub21
print(10000)