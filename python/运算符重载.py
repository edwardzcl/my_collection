class Mylist:
    def __init__(self, iterable=()):
        self.__data = list(iterable)
 
    def __repr__(self):
        return 'Mylist(%s)' % self.__data
 
    def __getitem__(self, i):
        '索引取值,i绑定[]内的元素'
        print('i的值', i)
        return self.__data[i]  # 返回data绑定列表中的第i个元素
 
    def __setitem__(self, i, v):
        '''此方法可以让自定义的列表支持索引赋值操作'''
        print('__setitem__被调用,i = ', i, 'v = ', v)
        self.__data[i] = v
 
    def __delitem__(self, i):
        del self.__data[i]  # self.__data.pop(i)
        return self
        if type(i) is int:
            print('用户正在用索引取值')
        elif type(i) is slice:
            print('用户正在用切片取值')
            print('切片的起点是:', i.start)
            print('切片的终点是:', i.stop)
            print('切片的步长是:', i.step)
        elif type(i) is str:
            print('用户正在用字符串进行索引操作')
            # raise KeyError
        return self.__data[i]  # 返回data绑定的第i个元素
 
 
l1 = Mylist([1, 2, 3, 4, -5, 6])
print(l1[3])  # 4
 
l1[3] = 400
print(l1)  # Mylist([1, 2, 3, 400, -5, 6])
 
del l1[3]
print(l1)  # Mylist([1, 2, 3, -5, 6])
 
print(l1[::2])  # [1,3,6]
