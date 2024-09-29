# Deletion at start of C.L.L

class node: 
    def __init__(self,data):
        self.info = data
        self.next = None

node1 = node(10)
node2 = node(20)
node3 = node(30)
node4 = node(40)
node5 = node(50)

node1.next = node2
node2.next = node3
node3.next = node4 
node4.next = node5
node5.next = node1

deleted = False

if node1 is None:
    print("Deletion not possible, L.L empty")
else:
    oldnode = node1
    data = oldnode.info
    if oldnode.next == node1:
        node1 = None
        deleted = True
    else:
        ptr = node1
        while ptr.next != node1:
            ptr = ptr.next 
        
        ptr.next = oldnode.next
        node1 = oldnode.next
        deleted = True
        
if deleted:
    ptr = node1
    while ptr is not None:
        print(ptr.info)
        ptr = ptr.next
        if ptr == node1:
            break
    print(f"Data {data} has been deleted")
else:
    print("Deletion not performed")