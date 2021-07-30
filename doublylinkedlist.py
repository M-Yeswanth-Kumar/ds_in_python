#              **************DoublyLinkedList*************

class Node:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left = left
        self.right = right

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_starting(self, element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
            return
        else:
           newNode.right = self.head
           self.head.left = newNode
           self.head = newNode

    def insert_at_end(self, element):
        newNode = Node(element)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.right != None:
                current = current.right
            current.right = newNode
            newNode.left = current
    def deleteNode(self, element):
        #base case
        if self.head == None:
            print("there is no value in the list")
            return



        #if only one node is present
        if self.head.right == None:
            if self.head.info == element:
                temp = self.head
                self.head = None
                temp = None
            else:
                print("the element is not present")
                return
        #delete node in between
        temp = self.head.right



        while temp.right != None:
            if temp.info == element:
                temp.left.right = temp.right
                temp.right.left = temp.left
                temp = None
                return
            temp = temp.right
        #to delete last node
        if temp.info == element:
            temp.left.right = None
            temp = None
            return
        print("the element is not present in the list")


    def delete(self, element):
        #base case
        if self.head == None:
            print("no elements are in the list")
            return

        #if one element present in the list
        if self.head.right == None:
            if self.head == element:
                temp = self.head
                self.head = None
                temp = None
                return
            else:
                print("element not found in the list")
                return

        #delete node in between
        temp = self.head.right

    def display(self):
        if self.head == None:
            print("the list is empty")
            return
        current = self.head
        while current != None:
            print(current.info)
            current = current.right


LL = LinkedList()
LL.insert_at_starting(10)
LL.insert_at_starting(20)
print("-------------------------------")
LL.insert_at_end(40)
LL.insert_at_end(50)
LL.display()
print("-------------------------------")
LL.deleteNode(867)
LL.display()