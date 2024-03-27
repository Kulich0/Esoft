def prov(str):
    stack = []  
    slovar = {')': '(', ']': '[', '}': '{'}  
    
    for char in str:
        if char in slovar:           
            if not stack or stack.pop() != slovar[char]:
                return False
        else:
            stack.append(char)   
    return not stack

print(prov("(]"))       
