""" https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true """

# We are reading the elemnts N and M, N = The size of the Array, M = Size of sets
n, m = map(int, input().split())

# Second line, this contains all the numbers in the array
array = list(map(int, input().split()))

# The third line, here we get the numbers We like
A = set(map(int, input().split()))

# The fourth line, here we get the numbers We DONT like
B = set(map(int, input().split()))

score = 0
for i in range(n):
    if array[i] in A:
        score += 1
    elif array[i] in B:
        score -= 1

print(score)


