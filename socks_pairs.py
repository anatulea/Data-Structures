'''
Alex works at a clothing store. 
There is a large pile of socks that must be paired by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.
For example, n= 7 there are  socks with colors . arr = [1,2,1,2,1,3,2] 
There is one pair of color  and one of color . 
There are three odd socks left, one of each color. 
The number of pairs is 2.

Function Description
Complete the sockMerchant function in the editor below. 
It must return an integer representing the number of matching pairs 
of socks that are available.

sockMerchant has the following parameter(s):
-- n: the number of socks in the pile
-- ar: the colors of each sock
'''

def sockMerchant(n, ar):
    total = 0
    n = int(input('Enter the number of socks in the pile: '))
    color = input('Enter the colors of each sock ').split(" ")
    for i in range(0, n):
        for j in range(i+1, n):
            if (color[i] == color[j] and color[i] != None):
                total = total+1
                color[j] = color[i] = None
                break

    print(total)

sockMerchant(None, None)

def sockMerchant2(color):
    total = 0
    color = input('Enter the colors of each sock ').split(" ")
    for i in range(0, len(color)):
        for j in range(i+1, len(color)):
            if (color[i] == color[j] and color[i] != None):
                total = total+1
                color[j] = color[i] = None
                break

    print(total)

sockMerchant2(None)


def sockMerchant3(n, ar):
    socks = {}
    pairs = 0
    for i in ar:
        if i not in socks.keys(): 
           socks[i] =1
        elif i in socks.keys():
            socks[i] += 1
        if socks[i]% 2 == 0:
            pairs += 1
    print (pairs)

colors = [6,7,8,5,6,6,8,7]
num = 7
sockMerchant3(num, colors)


def sockMerchant4(n, ar):
    seen = []
    matches = 0
    for color in ar:
        if color not in seen:
            seen.append(color)    
        else:
            seen.remove(color)
            matches += 1
    print (matches)
sockMerchant4(num, colors)