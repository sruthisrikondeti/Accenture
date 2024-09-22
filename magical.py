'''
You are given a program to find count of magical numbers from 1 
to N. A magical Number is defined by Following Criteria  
1. Replace 0 with 1 and 1 with 2 in binary string 
2. Calculate the sum of digits of modified binary string, if sum is odd it 
means its magical number. 
Input 1: 5 
Output 1: 2   
Explanation:  
1->1->2->even 
2->10->21->odd 
3->11->22->even 
'''
def magical(n):
    count=0
    sum=0
    for i in range(1,n):
        while(i>0):
            if(i&1):
                sum+=2
            else:
                sum+=1
            i>>=1
        if(sum%2!=0):
            count+=1
    return count-1
n=int(input())
print(magical(n))
    
