class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_pointer = -1
        for i in s:
            if (i in ['(','{','[']) or (len(stack)==0):
                stack.append(i)
                stack_pointer+=1
            else:
                if i == ')':
                    if stack[stack_pointer]!='(':
                        return False
                    else:
                        stack.pop()
                        stack_pointer-=1
                
                if i == '}':
                    if stack[stack_pointer]!='{':
                        return False
                    else:
                        stack.pop()
                        stack_pointer-=1

                if i == ']':
                    if stack[stack_pointer]!='[':
                        return False
                    else:
                        stack.pop()
                        stack_pointer-=1
        
        if len(stack) ==0:
            return True
        else:
            return False


        