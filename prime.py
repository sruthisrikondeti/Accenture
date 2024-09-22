'''prime number'''
def prime(n):
    count=0
    for i in range(1,n):
        if(n % i == 0):
            count+=1
    if(count<2):
        return ("prime")
    else:
        return "not prime"
    
n=int(input())
arr=[]
'''for i in range(n):
    x=int(input())
    arr.append(x)'''
print(prime(n))
