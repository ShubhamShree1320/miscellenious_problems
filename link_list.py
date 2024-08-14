class Linklist:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self) -> str:
        return (str(self.data))
    


head=Linklist(0)
a=Linklist(1)
b=Linklist(2)

head.next=a
a.next=b
curr=head # pointer used for traversing
while curr:
    if curr.data==1:
        new_node=Linklist(3)
        new_node.next=curr.next
        curr.next=new_node
    print(curr)
    curr=curr.next
