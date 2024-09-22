'''Question 2. Given an array of random numbers, Push all the zero’s of a given an 
array to the end of the array. All non-zero elements should come in front and 
Order of all non-zero elements should be same. 
Input Format: Given an array of random numbers. 
Output Format: Move all zeros to end of array and keeping all non-zero 
element in same position. 
Input 1:        
1   2  0   4  3  0   5  0 
Output 1:     1   2  4  3  5  0   0   0 
Input 1:        
1   2  0   0  0  3  6   
Output 1:     1   2  3  6  0  0   0   
'''
def Zeros_last(arr,n):
    narr=[]
    count=0
    for i in range(n):
        if(arr[i]!=0):
            narr.append(arr[i])
        else:
            count+=1
    for i in range(count):
        narr.append(0)
    return narr
    
n=int(input())
arr=[]
for i in range (n):
    x=int(input())
    arr.append(x)
print(Zeros_last(arr,n))
