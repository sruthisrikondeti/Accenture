"""There are no.of mangoes and no.of identical persons.How many ways are there to distribute the mangoes
Input:
Input1-no.of mangoes
Input2-no.of persons 
Input1:2
Input1:2
Output:
3
Explanation:
Ways:(1,1)(0,2)(2,0)"""

import math
m=int(input())
n=int(input())
def ways(m,n):
    if n==1 or m==0:
        return 1
    if n==0:
        return 0 
    return math.comb(m+n-1,n-1)
print(ways(m,n))
    
