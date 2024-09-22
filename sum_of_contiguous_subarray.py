'''A list of integers nums (1<=len(num)<=10^5) representing an array 
of numbers. Return the maximum sum of any contiguous subarray in the given 
array. 
Example:  
Input : -2  1  -3  4  -1  2  1  -5  4 
Output: 6 
Input : 3  -1  2  5  -6  3 
Output: 9
'''
def contiguous_sum(arr,n):
    res=arr[0]
    for i in range(n):
        cursum=0
        for j in range(i,n):
            cursum+=arr[j]
            res=max(res,cursum)
    return res
    
n=int(input())
arr=[]
for i in range (n):
    x=int(input())
    arr.append(x)
print(contiguous_sum(arr,n))
