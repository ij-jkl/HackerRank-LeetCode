""" https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true """

# Im not using it, hacker rank imports it
import textwrap

def wrap(string, max_width):
    # L and X are auxiliar variables, im going to be using them to keep track and adding them with the max width value
    l = 0
    

    result = []
    
    # We are doing this to keep iterating only the lenght of the string divided by the width of the words
    # Im dividing with // so i avoid floating numbers, the plus 1 its needed so it runs in all cases
    aux = len(string) // max_width + 1
    for _ in range(aux):
        #We append the strings from L to X, they have the lenght of the max width
        result.append(string[l:l + max_width])
        l += max_width

    return "\n".join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)