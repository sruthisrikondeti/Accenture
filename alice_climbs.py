'''Alice has to climb N stairs to reach top. In each step Alice can climb either 1 
step or M steps, Find the minimum numbers of steps to reach the top. 
Input Format: Input contains two space separated integer N and M. 
Output Format: Contains integer, that represents minimum number of climbs 
required to reach top. 
Constraints: 
1<=N<=10^9 
1<=M<=10^9 
 
Input 1: 6  4  
Output : 3
'''


def climbs(n,m):
    fullsteps=n//m
    rem=n%m
    return fullsteps+rem
n,  m=map(int,input().split())
print(climbs(n,m))
