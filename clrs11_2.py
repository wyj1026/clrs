class ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None
class hash_list(object):
    def __init__(self,k):
        self.li = []
        self.length=k//3
        for i in range(k//3):
            self.li.append(None)
    def hash(self,case):
        return case.val%self.length
    def insert(self,case):
        k = self.hash(case)
        if self.li[k]==None:
            self.li[k]=case
        else:
            VAL=self.li[k]
            while VAL.next:
                VAL=VAL.next
            VAL.next = case

