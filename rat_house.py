r=int(input())
unit=int(input())
n=int(input())
arr=[]
for i in range(n):
    x=int(input())
    arr.append(x)
def rat_houses(r,unit,arr,n):
    foodtillnow=0
    house=0
    total_food=r*unit
    if(n==0):
        return -1
    for house in range (n):
        foodtillnow+=arr[house]
        if(foodtillnow>=total_food):
            break
    if(total_food>foodtillnow):
        return 0
    return house+1 
            

print (rat_houses(r,unit,arr,n))            
           
        
