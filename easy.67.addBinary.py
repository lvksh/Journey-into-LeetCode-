class Solution:
    def addBinary(self, a: str, b: str):
        diff = abs(len(a) - len(b))
        if len(a) < len(b):
            a = '0'*diff + a
        else:
            b = '0'*diff + b
        
    
