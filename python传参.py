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