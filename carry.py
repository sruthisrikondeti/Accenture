'''Problem Statement

A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time

You are required to implement the following function.

Int NumberOfCarries(int num1 , int num2);

The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.

Assumption: num1, num2>=0

Example:

Input
Num 1: 451
Num 2: 349
Output
2
Explanation:

Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.

Sample Input

Num 1: 23

Num 2: 563

Sample Output

0
'''

def number_carry(n1,n2):
    carry=0
    count=0
    while(n1>0 or n2>0):
        num1=n1%10
        num2=n2%10
        sum=num1+num2+carry
        if sum>9:
            count+=1
            carry+=1
        else:
            carry=0 
        n1=n1/10
        n2=n2/10
    return count

n1=int(input())
n2=int(input())

print(number_carry(n1,n2))
    
        
