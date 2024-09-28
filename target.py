''' Find the target element in an array. 
int [] array = {2,3,4,10,40}; 
int target = 10;
'''
def find_target(arr,tar):
    n=len(arr)
    if(n==0):
        print("enter inputs")
    for i in range (n):
        if(arr[i]==tar):
            print("element found in index:",i)
        
n=int(input())
arr=[]
for i in range (n):
    x=int(input())
    arr.append(x)

tar=int(input())
find_target(arr,tar)
