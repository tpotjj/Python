class Node:
    def __init__(self, value=None):
        self.value = value
        self.next= None

class SinlgeLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode


sll =  SinlgeLinkedList()
sll.insertSLL(1,1)
sll.insertSLL(2,1)
sll.insertSLL(3,1)
sll.insertSLL(4,1)


sll.insertSLL(0,3)


print([node.value for node in sll])