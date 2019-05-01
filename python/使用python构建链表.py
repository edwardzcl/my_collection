"""
本文参考自：https://mp.weixin.qq.com/s/4gxszokInvLzfUt8cyWeAA
Python 中由于不存在指针，所以指针和链表指的都是模拟指针和链表。所以这里的常见操作应当加上链表的构建操作。
"""

class Node(object):
    """
    定义一个节点类
    """
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkList(object):
    """
    创建一个链表类，包括判断是否为空、打印链表
    """
    def __init__(self):
        self.head = Node(None) 

    def InitList(self, data):
        if len(data) == 0:
            print('\nIt is a empty link list')
            return False

        self.head = Node(data[0])#头结点，data的一个元素为数据域信息
        p = self.head #头指针，指向第一个结点

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next


    def IsEmpty(self):
        p = self.head #指向第一个结点    
        if p == None:
#           print('\nIt is a empty link list')
            return True #是空链表    
#       print('\nIt is not empty')
        return False #非空链表

    def PrintList(self):
        p = self.head

        while p: #注意不是p.next
            print(p.data) #end表示结束的标识，不添加说明时默认为换行符
            p = p.next 

    def Size(self):
        """
        求取链表长度
        """
        p = self.head
        size = 0

        while p:
            size += 1
            p = p.next
        return size 

    def Del(self,n):

        if self.IsEmpty() or n < 0 or n > self.Size():
           print('error occured')
           return

        p = self.head 

        if p.next is None:   # 当只有一个节点的链表时
           self.head = None
           return        

        if n == 1:   # 当删除第一个节点时
           self.head = p.next
           return

        #普通情况
        p = self.head        
        index = 1
        while index < n:#找到要删除的结点位置
              pre = p
              index += 1
              p = p.next     
        pre.next = p.next#跳过该结点即可删除
        p = None 

    def Insert(self,n,data):

        if n < 0 or n > self.Size() + 1: 
        #n最小值为0，且插入位置超过长度+1时实际只能插入到最后，即最大值为链表长【0，size】区间内有效
           print('error occured')
           return

        p = self.head

        if self.IsEmpty():#空链表时插入头指针之后即可
           node = Node(data)
           p.next = node
           return

        if n == 0:
           node = Node(data)
           lat = self.head
           self.head = node #新插入的做头结点
           node.next = lat #新插入结点后续指向之前的头结点
           return

        index = 1
        while index < n:
              index += 1
              p = p.next

        #插入操作关键之处，注意指针变换顺序
              node = Node(data)
        node.next = p.next
        p.next = node  




class Solution:
    """
    leetcode题目中提交函数都只用放在此类下
    """
    def reverseList(self, head):
        """
        翻转操作leetcode题目206
        """
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
            #这一行等同于如下 4 行：
            #lat = cur.next
            #cur.next = pre
            #pre = cur
            #cur = lat

        return pre


def main():
    """ 
    测试
    """
    data = [100, 2, 300, 4, 500]    
    lst = LinkList()
    lst.InitList(data)
    lst.PrintList()

    print("reverse")
    lst.head = Solution().reverseList(lst.head)
    lst.PrintList()


main()
