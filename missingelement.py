'''. Find the missing number in an array. 
Given an array nums containing n distinct numbers in the range [0,n], return 
the only number in the range that is missing from the array. 
Input: Nums = [3,0,1] 
Output: 2 
'''
def missing(arr,n):
    if(n==0):
        print("enter inputs")
    arr.sort()
    for i in range (0,n):
        if(arr[i]==i):
            print()
        else:
            return i
        
n=int(input())
arr=[]
for i in range (n):
    x=int(input())
    arr.append(x)
print(missing(arr,n))
