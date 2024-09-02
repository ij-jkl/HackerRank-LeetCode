"""  https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true  """

# We read N as the amount of numbers of the input
n = int(input())
# Sets do not have two of the same data
total = set()

for i in range(n):

    # We are reading the input and striping them from any spaces from the variable
    i = input().strip()
    total.add(i)

print(len(total))