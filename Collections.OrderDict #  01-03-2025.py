"""https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true"""

# Solution passes 100% Test cases.

from collections import OrderedDict

# Number of items
n = int(input())

# Empty order direct to store items and prices.
ordered_dict = OrderedDict()

for _ in range(n):
    # Split the text and price, first we get the item name and then the price
    *item_name, price = input().split()
    item_name = " ".join(item_name)
    price = int(price)

    # If an item is already in the dictionarie we update the price, if not we add it
    if item_name in ordered_dict:
        ordered_dict[item_name] += price
    else:
        ordered_dict[item_name] = price

# Print and Submit exercise
for item_name, net_price in ordered_dict.items():
    print(item_name, net_price)

"""
Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
"""

""" 
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""