#Q1 - 
'''check vowel or not'''
c = 'a'

# checking for vowels
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
    print(c, "is a vowel")  # condition true input is vowel
else:
    print(c, "is a consonant") 
#a is a vowel
'''Q2-Python program to check whether a character is an alphabet or not'''
# Python Program to find character is alphabet or not

# user input
ch = 'z'

# basic logic
if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print("The  character", ch, "is an Alphabet")
else:
    print("The  character", ch, "is not an Alphabet")
'''Output
The  character z is an Alphabet'''
#Q3 palindrome or not
s1=input()
s2=s1[::-1]
if(s1==s2):
    print("palindrome")
else:
    print("not palindrome")
#Q4 change order of words
def reverse_words(input_str):
    words = input_str.split()
    reversed_words = words[::-1]
    reversed_str = ' '.join(reversed_words)
    return reversed_str

input_str =input()
result = reverse_words(input_str)
print(result)
