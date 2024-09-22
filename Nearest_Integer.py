'''Int nearestInteger(int num, int m) 
The function accepts two positive ‘num’ and ‘m’ as its argument, Implement 
the following function to find the nearest integer to num. 
1) Number is divisible by m. 
2) Number is nearest to ‘num’ (Have the least distance from num) 
Note: If there are two numbers with the least distance from num, then return 
the larger num. 
Input 1: Num= 67 
M = 8 
Output 1: 64 
Input 2: Num=26 
M=3 
Output 2: 27
'''
def nearest_integer(num,m):
    narr=[]
    for i in range(num//2,num+m):
        if(i%m==0):
            narr.append(i)
    n=len(narr)
    res=0
    if((narr[n-1]-num)<(num-narr[n-2])):
        res=narr[n-1]
    elif((narr[n-1]-num)==(num-narr[n-2])):
        res=max(narr[n-1],narr[n-2]) 
    else:
        res=narr[n-2]
    return res
num =int(input())
m =int(input())
print(nearest_integer(num,m))
