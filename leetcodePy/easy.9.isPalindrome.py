def isPalindrome(x):
    a = list(str(x))
    b = list(reversed(a))
    if a == b:
        return ('true')
    else:
        return ('false')
    
x = -121
isPalindrome(x)    