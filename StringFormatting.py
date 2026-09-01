#The question
'''
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

Input Format

A single integer denoting .

Constraints

Sample Input

17
Sample Output

    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
'''

#My Solution

def convert(number, base):
    base_list = []
    base_value = 0
    while_breaker = 0
    
    while number >= 1 or while_breaker < 50:
        base_value = number % base
        
        number = (number / 2) - base_value
        
        base_list.append(base_value)
    
    output = ''
    for i in range(0, len(base_list)):
        output = output + str(base_list[i])
        
    
    return output
    

        
            
def print_formatted(number):
    
    for i in range(0, number):
        
        n
        binary_val = convert(i, 2)
        octal_val = convert(i, 8)
        
        print(i + '   ' + octal_val + '     ' + binary_val)


#The actual solution

def print_formatted(n):
    width = len(bin(n)[2:])   # length of binary representation of n
    
    for i in range(1, n + 1):
        deci = str(i).rjust(width)
        octa = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        bina = bin(i)[2:].rjust(width)
        
        print(deci, octa, hexa, bina) 
