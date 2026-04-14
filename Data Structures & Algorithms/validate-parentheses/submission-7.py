class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dict = { '}' : '{', ']' : '[', ')' : '(' }
      
        for x in s:
            if x in dict:
                if stack and stack[-1] == dict[x]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
    
        if not stack:
            return True
        else:
            return False

        


        


            

        

