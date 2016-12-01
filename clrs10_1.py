class Stack(object):
    def __init__(self):
        self.items=[]
        self.top = None
    def empty(self):
        return len(self.items) == 0
    def push(self,x):
        self.items.append(x)
        self.top = x
    def pop(self):
        if len(self.items)==1:
            self.top=None
        else:
            self.top = self.items[-2]
        return self.items.pop()

class Queue(object):
    def __init__(self):
        self.items = []
        self.head = None
        self.tail = None
    def empty(self):
        return len(self.items)==0
    def push(self,x):
        if self.empty():
            self.head,self.tail = x,x
            self.items.append(x)
        else:
            self.items.append(x)
            self.tail = x
    def pop(self):
        if self.empty():
            raise TypeError("the Queue is empty")
        elif len(self.items)==1:
            self.head,self.tail = None,None
            return self.items.pop()
        else:
            self.head = self.items[1]
            return self.items.pop(0)
