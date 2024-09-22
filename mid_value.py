'''print mid value of sorted positive array from given array'''

def mid_value(arr):
    narr=[]
    for i in arr:
        if(i>=0):
            narr.append(i)
    narr.sort()
    n1=len(narr)
    if(n1%2==0):
        return narr[(n1//2)-1]
    else:
        return narr[n1//2]
n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
print(mid_value(arr))
