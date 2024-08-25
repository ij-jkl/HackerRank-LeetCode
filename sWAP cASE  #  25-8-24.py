""" https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true """

def swap_case(s):
    # List
    result = []
    
    # Looping through the entire word
    for i in s:
        #If its a lower letter we make it an Upper case, else its upper word to Lower case
        if(i.islower()):
            result.append(i.upper())
        else:
            result.append(i.lower())
            
     #Needed for good output       
    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)