'''You are required to implement the following Function 

def LargeSmallSum(arr)

The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest  element from the even positions and second smallest from the odd position of given ‘arr’

Assumption:

All array elements are unique
Treat the 0th position as even
NOTE

Return 0 if array is empty
Return 0, if array length is 3 or less than 3
Example

Input

arr:3 2 1 7 5 4

Output

7

Explanation

Second largest among even position elements(1 3 5) is 3
Second smallest among odd position element is 4
Thus output is 3+4 = 7
Sample Input

arr:1 8 0 2 3 5 6

Sample Output

8
'''

def even_odd():
    arr=[]
    even=[]
    odd=[]
    n=int(input())
    if (n==0 or n<=3):
        return 0
    for i in range (n):
        x=int(input())
        arr.append(x)
    
    for i in range (n):
        if(i>0):
            if(i%2==0):
                even.append(i)
            else:
                odd.append(i)
    even.sort()
    odd.sort()
    print(even[len(even)-2]+odd[len(odd)-2])
    
even_odd()
