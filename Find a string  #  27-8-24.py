"""  https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true """

def count_substring(string, sub_string):
    
    #Define the lenght of the Sub string that we are trying to find in the String
    total = 0
    subStringLen = len(sub_string)
    
    #We do a for loop with the length of the String
    for i in range(len(string)):

        #We check if the string from I = 0, to I = 0 + 3 is equal to sub_string
        if(string[i:i + subStringLen] == sub_string):
            total += 1
    return total

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)