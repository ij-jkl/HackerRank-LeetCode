""" https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true """

from collections import Counter


numberShoes = int(input()) 
sizeShoes = input().split() 
countedShoes = Counter(sizeShoes)

numberCustomers = int(input())

totalMoney = 0


for i in range(numberCustomers):
    # Price and Size of each customer
    size, price = input().split()
    price = int(price)
    
    if countedShoes[size] > 0:
        # If so we eliminate one of the remaining stock of that size
        countedShoes[size] -= 1  
        totalMoney += price  

print(totalMoney)
