""" https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true """

def split_and_join(line):
    
    #Checking for empty spaces and replacing them with -
    line = line.replace(" ","-")
    
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)