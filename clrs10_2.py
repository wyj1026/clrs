class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None
    def search(self,key):
        A = self
        while not A.val==key:
            A=A.next
        return A
    def insert(self,key):
        A = ListNode(key)
        A.next = self
        return A
