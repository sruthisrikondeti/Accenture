#Q1
n = 5  # Number of rows

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1 or i == n or j == 1 or j == n:
            print("5", end=" ")
        else:
            print(" ", end=" ")
    print()
  '''output
5 5 5 5 5 
5       5 
5       5 
5       5 
5 5 5 5 5 
'''
#Q2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
#Q3
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''
#Q4
 n = 5

for i in range(n):
    # Print spaces
    print(" " * (n - i - 1), end="")

    # Print ascending numbers
    for k in range(1, i + 2):
        print(k, end="")

    # Print descending numbers
    for l in range(i, 0, -1):
        print(l, end="")

    # Move to the next line
    print()
  '''
    1
   121
  12321
 1234321
123454321
'''
#Q5
n = 5

for i in range(n, 0, -1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print the number pattern
    for k in range(1, i * 2):
        print(k, end="")

    # Move to the next line
    print()
  '''
123456789
 1234567
  12345
   123
    1
    '''
#Q6
n = 5

# Upper half of the diamond
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for k in range(1, i * 2):
        print(k, end="")
    print()

# Lower half of the diamond
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for k in range(1, i * 2):
        print(k, end="")
    print()
  '''
    1
   123
  12345
 1234567
123456789
 1234567
  12345
   123
    1
'''
