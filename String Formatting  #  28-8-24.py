""" https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true """

def print_formatted(number):
    
    # We need this padding to pass the output expected by Hacker Rank
    # I have to pass the number as a Binary number or its not going to pass All test cases
    space = len(bin(number)[2:])

    for i in range(number):
        decimal = str(i+1)
        # I use the [2:] because if not the output looks like this ( 0o1 ), instead of : 1
        octal = oct(i+1)[2:]
        hexadecimal = hex(i+1)[2:].upper()
        binary = bin(i+1)[2:]

        #I used chat gpt to figure out how to correctly use rjust for the output, as I didnt know how to print it as expected
        print(decimal.rjust(space),octal.rjust(space),hexadecimal.rjust(space),binary.rjust(space))
        

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)