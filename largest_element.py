'''
 Find the largest number in an array 
Int arr[]= {1,4,6,7,8,9} 
Output: 9
'''


def largest_element(arr):
    max=arr[0]
    for i in range(n):
        if(arr[i]>max):
            max=arr[i]
    return max
n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
print(largest_element(arr))
