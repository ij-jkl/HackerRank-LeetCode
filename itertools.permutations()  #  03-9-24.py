"""  https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true  """

from itertools import permutations

#We take the first input as the word, and the second as the Length of the words
s = input()
word = s.split()[0]
lenngth = int(s.split()[1])

#We sort the list and use the permutations function, we pass as parameters the Word itself and the Len of the words
permu = sorted(list(permutations(word,lenngth)))

#We loop through the variable, and we use a join to have the Desired output
for p in permu:
    print("".join(p))