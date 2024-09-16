'''Question: Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate palindrome numbers.

Test Cases:

TestCase 1:
Input :
10 , 80
Expected Result:
11 , 22 , 33 , 44 , 55 , 66 , 77.

Test Case 2:
Input:
100,200
Expected Result:
101 , 111 , 121 , 131 , 141 , 151 , 161 , 171 , 181 , 191.'''
def ispal(n):
    temp=n
    rev=0
    while temp>0:
        digit=temp%10
        rev=(rev*10)+digit
        temp=temp//10
    if n==rev:
        return n
n1=int(input())
n2=int(input())
arr=[]
for i in range(n1,n2+1):
    if(ispal(i)):
        arr.append(str(i))
print(','.join(arr))
