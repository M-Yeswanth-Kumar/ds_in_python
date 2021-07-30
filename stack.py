class Stack:
    def __init__(self):
        self.stack = []

    def  isEmpty(self):
        return self.stack == []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

s = Stack()

while True:
    print("push")
    print("pop")
    print("peek")
    do = input("what exactly you want to perform?")
    if do == "push":
        element = int(input("enter the element you want to insert"))
        s.push(element)
    elif do == "pop":
        element = s.pop()
        if element  == -1:
            print("your stack is empty")
        else:
            print("deleted element in the stack is {}".format(element))
    elif do == "peek":
        element = s.peek()
        if element == -1:
            print("stack is empty")
        else:
            print("Top of the stack is {}".format(element))

    else:
        break



