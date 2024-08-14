class Link:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    

obj=Link(1)
obj.next=Link(2)
obj.next.next=Link(3)
curr=obj
prev=None

while curr:
    tmp=curr.next
    curr.next=prev
    prev=curr
    curr=tmp
print(prev)