#    ******** Parenthesis check *******
# Parenthesis check is an application of stack .

class parenthesis:
    def __init__(self):
        self.stack = []

    def check(self, expression):
        for i in range(len(expression)):
            if expression[i] == "(" or expression[i] == "["  or expression[i] == "{":
                self.stack.append(expression[i])
                continue

            if len(self.stack) == 0:
                return False

            if expression[i] == ")":
                char = self.stack.pop()
                if char != "(":
                    return False

            if expression[i] == "]":
                char = self.stack.pop()
                if char != "[":
                    return False

            if expression[i] == "}":
                char = self.stack.pop()
                if char != "{":
                    return False

        if len(self.stack):
            return False
        else:
            return True

p = parenthesis()

expression = input("enter the expression:")
if p.check(expression):
    print("this is a valid expression")
else:
    print("the expression is not valid")


