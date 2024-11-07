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
def is_magical(num):
    # Convert to binary and remove the '0b' prefix
    binary_str = bin(num)[2:]
    # Replace 0 with 1 and 1 with 2
    modified_str = binary_str.replace('0', '1').replace('1', '2')
    
    # Calculate the sum of the digits in the modified string using a loop
    digit_sum = 0
    for digit in modified_str:
        digit_sum += int(digit)
    
    # Check if the sum is odd
    return digit_sum % 2 == 1

def count_magical_numbers(N):
    count = 0
    for i in range(1, N + 1):
        if is_magical(i):
            count += 1
    return count

# Example usage
N = 10
print(count_magical_numbers(N))  # Output the count of magical numbers from 1 to N

    
