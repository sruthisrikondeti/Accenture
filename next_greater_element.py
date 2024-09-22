'''1. Given an array of N size, Print the Next Greater Element of every 
element. 
The Next Great Element for an element x is the first greater element on the 
right side of x in the array. Elements for which no greater element exist, 
consider the next greater element as -1 
Input Format: Given array of N size with space separated integers. 
Output: Array of size N with next greater element. 
Input 1: 4 5 2 25 
Output 1: 5 25 25 -1 
Input 2: 5 7 1 7 6 0 
Output 2: 7 -1 7 -1 -1 -1
'''

def greater_element(arr):
    narr=[]
    for i in range(0,n):
        x=arr[i]
        for j in range(i+1,n):
            if(x<arr[j]):
                narr.append(arr[j])
                break
            else:
                narr.append(-1)
                break
    if(len(narr)<n):
        narr.append(-1)
    return narr
    
n=int(input())
arr=[]
for i in range (n):
    x=int(input())
    arr.append(x)
print(greater_element(arr))

    
