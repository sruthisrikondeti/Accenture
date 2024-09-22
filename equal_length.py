'''Given an array of length n, find the length of largest subarray 
which contains equal number of 0s and 1s  
Input 1->     1   0   1   1   1   0   0 
Output 1->   6 
 
Input 2:     0   0   1   1   0 
Output:     4
'''
def array_largest(arr):
    count_0=0
    count_1=0
    
    for i in arr:
        if(i==0):
            count_0+=1
        else:
            count_1+=1
    if(count_1<count_0):
        return count_1*2
    else:
        return count_0*2

n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
print(array_largest(arr))
