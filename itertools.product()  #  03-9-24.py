"""  https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true  """

# This is my code and it works, but hacker rank doesnt allow that output format

#from itertools import product
#listA = input()
#listB = input()
#lista = list(product(listA.split(),listB.split()))
#print(lista)

from itertools import product

#Split each List
listA = input().split()
listB = input().split()

#Need to convert each number into an integer so we can List it
listA = [int(i) for i in listA]
listB = [int(i) for i in listB]

#We use the product function from itertools
lista = list(product(listA,listB))

#We use a join, and we loop through each number converting it to a string so we can print it in the Desired output
print(" ".join(str(t) for t in lista))
