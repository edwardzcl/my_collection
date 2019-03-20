"""
以下内容为关于可变对象与不可变对象，以及自定义对象作为函数参数传递时，原始变量(别名，引用名称)如何变化
更多请参考：https://blog.csdn.net/edward_zcl/article/details/88697763
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

"""
以下内容为类与对象的关系，类变量与对象变量的区别
"""

###############        警告：不要看后面的注释，是错的           ##################

class Man(object):
    #直接定义的类的变量，属于类   
    #其中 gender, avg_height为基本数据类型，immutable
    #lis为列表类型，为mutable的
    gender = 'male'   
    avg_height = 1.75
    lis = ['hello', 'world']
 
    def __init__(self, name):
        self.name = name  #name在类的构造函数中定义，是属于对象的变量
 
    
a = Man('jason')
b = Man('tom')
 
#通过一个对象a访问一个变量x，变量的查找过程是这样的：
#先在对象自身的__dict__中查找是否有x，如果有则返回，否则进入对象a所属的类A的
#__dict__中进行查找
 
#对象a试图修改一个属于类的 immutable的变量，则python会在内存中为对象a
#新建一个gender变量，此时a就具有了属于自己的gender变量
a.gender = 'female'
 
#对象b试图修改一个mutable的变量，则python找到类Man的__dict__中的变量lis，
#由于lis是可以修改的，因此直接进行修改，而不会给b新生成一个变量。类Man以及类Man
#的所有对象都公用这一个lis
b.lis = ['fuck', 'world']
 
print (a.__dict__) #属于a的变量，有 name， gender
print (b.__dict__)  #属于b的变量，只有name
print (Man.__dict__) #属于类Man的变量，有 gender，avg_height，lis，但是不包括 name
#name是属于对象的变量
 
Man.t = 'test' #此时Man的变量又多了t，但是对象a和b中没有变量t。
#（这里可以看出，对象的变量和类的变量是分开的）
 
print (a.gender)  #female
print (b.gender)  #male
 
print (a.lis) #['fuck', 'world']
print (b.lis) #['fuck', 'world']
print(Man.lis)
 
a.addr = '182.109.23.1' #给对象a定义一个变量，对象b和类Man中都不会出现（解释性语言好随性。。）
a.lis.append(100)
print (a.lis) #['fuck', 'world']
print (b.lis) #['fuck', 'world']
print(Man.lis)

a.lis=[100]
print (a.lis) #['fuck', 'world']
print (b.lis) #['fuck', 'world']
print(Man.lis)

print(a.t)
print(b.t)
print(Man.t)


"""
以下为类方法，静态方法，对象方法的区别
"""
class A(object):
    bar = 1
    def foo(self):
        print ('foo')
 
    @staticmethod
    def static_foo():
        print ('static_foo')
        print (A.bar)
 
    @classmethod
    def class_foo(cls):
        print ('class_foo')
        print (cls.bar)
        cls().foo()
 
A.static_foo()
A.class_foo()


"""
以下为类的继承，以及类实际的构造方法 __new__ 的使用
"""

class task_queue:
    queue=[]
    
    def append(self,obj):
        self.queue.append(obj)
        
    def print_queue(self):
        print self.queue
        


a=task_queue()
b=task_queue()
c=task_queue()
    
a.append('tc_1')
    
a.print_queue()
b.print_queue()
c.print_queue()


class task_queue:
    
    def __init__(self):
        self.queue=[]
    
    def append(self,obj):
        self.queue.append(obj)
        
    def print_queue(self):
        print self.queue


a=task_queue()
b=task_queue()
c=task_queue()
    
a.append('tc_1')
    
a.print_queue()
b.print_queue()
c.print_queue()


class a():  
    num = 0  

    
obj1 = a()  
obj2 = a()   
print obj1.num, obj2.num, a.num   
          
obj1.num += 1  
print obj1.num, obj2.num, a.num     
      
a.num += 2  
print obj1.num, obj2.num, a.num

class ClassTest(object):
    __num = 0

    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
    def __new__(self):
        ClassTest.addNum()
        return super(ClassTest, self).__new__(self)


class Student(ClassTest):
    def __init__(self):
        self.name = ''

a = Student()
b = Student()

print(ClassTest.getNum())


