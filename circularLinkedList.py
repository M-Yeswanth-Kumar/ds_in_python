#                          ********** circular Linked List  *************

class Node:
   def __init__(self, info, next = None):
       self.info = info
       self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, element):

        newNode = Node(element)

        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head
            self.head = newNode

    def insert_at_end(self, element):
        newNode = Node(element)

        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head

    def display(self):
        current = self.head

        while current.next != self.head:
             print(current.info)
             current = current.next
        print(current.info)

    def deleteNode(self,element):
        if self.head == None:
            print("the element is not present in the list")
            return
        if self.head.info == element:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        current = self.head
        while current.next != self.head:
            if current.next.info == element:
                temp = current.next
                current.next = temp.next
                temp = None
                return
            current = current.next
        print("the element is not present in the list")



LL = LinkedList()
LL.insert_at_begining(10)
LL.insert_at_begining(20)
LL.insert_at_begining(25)
LL.display()
print("***")

LL.insert_at_end(30)
LL.insert_at_end(35)
LL.insert_at_end(40)

LL.display()


print("***")

LL.deleteNode(20)
LL.deleteNode(40)
LL.display()
