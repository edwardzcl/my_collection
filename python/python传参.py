"""
以下内容为关于可变对象与不可变对象，以及自定义对象作为函数参数传递时，原始变量(别名，引用名称)如何变化
"""

a=100
def add(x):
    x+=200
    return x


b=add(a)
print(a)
print(b)

a=[1,2,3]
def add(x):
    x=[1,2]
    return x

b=add(a)

print(a)
print(b)

a=[1,2,3]
def add(x):
    x+=[100]
    return x

b=add(a)

print(a)
print(b)

a=[1,2,3]
def add(x):
    x.append(100)
    return x

b=add(a)

print(a)
print(b)

a=[1,2,3]
def add(x):
    x=x+[100]
    return x

b=add(a)

print(a)
print(b)


class Node(object):
    """
    定义一个节点类
    """
    def __init__(self,data):
        self.data = data

a=Node([1,2,3])
print(a.data)

def add(x):
    x=100

add(a)    
print(a.data)

a=Node([1,2,3])
def add(x):
    x.append(1000)

add(a.data)
print(a.data)

a=Node([1,2,3])
def add(x):
    x=[100]
    return x

b=add(a.data)
print(a.data)
print(b)


a=Node([1,2,3])
def add(x):
    x.data=100
    x.app=[2,3,4]
    x.app.append(10000)
    q=x
    q.data=[100,200,300]

add(a)
print(a.data)
print(a.app)


a=Node([1,2,3])
def add(x):
    a=x.data
    a.append(100)

add(a)
print(a.data)

a=Node([1,2,3])
def add(x):
    a=x.data
    a=100

add(a)
print(a.data)


a=Node([1,2,3])
def add(x):
    a=x.data
    return a

b=add(a)
print(a.data)
print(b)
b.append(100)
print(a.data)
print(b)


"""
更多内容请参考我的博客以及相关公众号内容：
https://blog.csdn.net/edward_zcl/article/details/88382319
https://blog.csdn.net/edward_zcl/article/details/88697763

https://mp.weixin.qq.com/s/0gkQipK_0zoITBHv6XxOWA
https://mp.weixin.qq.com/s/eE8u4mpkRz_FOY5CxVfWog
https://mp.weixin.qq.com/s/w0NoDiYfvtTy8N3BVoIVpw
https://mp.weixin.qq.com/s/7qax1g621MTdKnJbP1SWhQ
https://mp.weixin.qq.com/s/0gkQipK_0zoITBHv6XxOWA
https://mp.weixin.qq.com/s/MGNUax9F5IFWW-Ouz9L7GQ
https://mp.weixin.qq.com/s/oWchI5QBuLUgvXXs-o5EWA
https://mp.weixin.qq.com/s/KNTmQVhKj2fYSQ-kokQ5pA
https://mp.weixin.qq.com/s?__biz=Mzg2NzE1NTQwNQ==&mid=2247488071&amp;idx=1&amp;sn=fa300ce328b0d894158de188e9c2b701&source=41#wechat_redirect
https://mp.weixin.qq.com/s/AbbCo5eL3vh-FsZxUWbMZQ
https://mp.weixin.qq.com/s/DOBG0yF0y8CwodCky_LALA
https://mp.weixin.qq.com/s/dbKBu3Jr_hYpRhhFzbpNKg
https://mp.weixin.qq.com/s/DOBG0yF0y8CwodCky_LALA
"""