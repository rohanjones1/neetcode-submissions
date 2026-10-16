class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if (i == "(" or i == "[" or i == "{"):
                stack.append(i)
            else:
                if (stack):
                    top = stack[-1]
                else:
                    return False
                if (i == ")"):
                    if (top == "("):
                        stack.pop()
                    else:
                        return False
                if (i == "]"):
                    if (top == "["):
                        stack.pop()
                    else:
                        return False
                if (i == "}"):
                    if (top == "{"):
                        stack.pop()
                    else:
                        return False
        if stack:
            return False
        return True
                