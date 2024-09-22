''' Reverse a Number  
Num= 987654 
Output= 456789
'''
def reverse(n):
    rev=0
    while(n>0):
        digit=n%10
        rev=rev*10+digit
        n//=10
    return rev
    
n=int(input())
print(reverse(n))
    
