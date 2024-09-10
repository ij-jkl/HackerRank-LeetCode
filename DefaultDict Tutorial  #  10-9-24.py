""" https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true """

from collections import defaultdict

# We read the length of each group
groupA, groupB = map(int, input().split())
d = defaultdict(list)


for i in range(groupA):
    # We read the input and we assign it to an auxiliar
    aux = input()
    # If its a list we can just do d.append(aux)
    # Here we need to do the i+1 or else it wont pass the Test cases
    # We use the aux in d[aux] because thats going to be our Key value
    d[aux].append(i+1)

for i in range(groupB):
    aux = input()
    # If the value is in the other group we just print it, else we print -1
    if(aux in d):
        # Using the * helps out in the desired output, going from [1, 2, 4] [3, 5] to 1 2 4 3 5
        print(*d[aux])
    else:
        print(-1)


"""
Sample Input
5 2     
a       
a
b
a
b
a       
b """

""" 
Sample Output
1 2 4
3 5 """