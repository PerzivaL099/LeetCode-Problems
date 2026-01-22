class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #valid operations + - * /
        stack = []
        #Cases for operations
        for i in tokens:
            match i:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
                case _:
                    #when a token \= from number
                    stack.append(int(i))

        return stack[0]
        #if i in List == int 
            #push into stack
        #else if i in List == operator
            #pop last 2 elements
            #apply operation
            #push result into stack