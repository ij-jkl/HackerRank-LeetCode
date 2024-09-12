""" https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true """

numberLength = input()
array = []

# We append the amount of numbers indicated by numberLenght (The first number) 
for i in range(int(numberLength)):
    array.append(input())


for i in range(int(numberLength)):
    # We try to assign the numbers and divide them, we need to use // in the division for the outputs
    try:
        number1 = int(array[i].split()[0])
        number2 = int(array[i].split()[1])
    
        print(number1//number2)
        
    except Exception as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

""" 
Sample Input
3
1 0
2 $
3 1 
"""

"""
Expected Output 
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
"""