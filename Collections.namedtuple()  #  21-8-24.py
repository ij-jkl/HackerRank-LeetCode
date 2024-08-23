""" https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true """

from collections import namedtuple

n = int(input())
cols = input().split()

index = cols.index("MARKS")

Students = namedtuple("students", "ID,MARKS,CLASS,NAME")

avgScores = 0

for i in range(n):
    Students = namedtuple("NAME", "MARKS")
    students = Students(MARKS=int(input().split()[index]))
    avgScores = avgScores + students.MARKS

print(round(avgScores/n, 2))
    
