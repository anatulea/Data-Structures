''' 
Given two strings, write a function to determine if the second string
is an ANAGRAM of the first. The number of letters must match (frequency pattern).
Return True or False
'''
'''
test examples:
validAnagram('','') // true
validAnagram('aaz', 'zza') // false
validAnagram('anagram', 'nagaram') // true
''' 
def validAnagram(firstString, secondString):  
   # check if the strings have the same length
   # if they don't return false 
    if len(firstString) != len(secondString) :  
        return False
  
    # sort the strings  
    firstString = sorted(firstString.lower()) 
    secondString = sorted(secondString.lower())  

    # compare the sorted strings 
    for i in range(0, len(firstString)):  
        if firstString[i] != secondString[i]:  
            return False
  
    return True

print(validAnagram('','') )
print(validAnagram('aaz', 'zza'))
print(validAnagram('anagram', 'nagaram'))   
print(validAnagram('AnaGram', 'nagaram')) 

print("-----Method 2------")
# method 2
def Anagram(str1, str2):
    if(sorted(str1) == sorted(str2)):
        print("True")
    else:
        print("False")

Anagram('','')
Anagram('aaz', 'zza')
Anagram('anagram', 'nagaram')  
Anagram('AnaGram', 'nagaram') 

# Method 3
print("----- Method 3 ------")
def validAnagram3(str1, str2):
    # true if matching number of letters
    # use dictionary to store number of letters
    # compare dictionary1 to dictionary 2
    dictionary1 = {}
    dictionary2 = {}
    for letter in str1:
        if letter not in dictionary1.keys():
            dictionary1[letter] = 1
        else:
            dictionary1[letter] += 1
    for letter in str2:
        if letter not in dictionary2.keys():
            dictionary2[letter] = 1
        else:
            dictionary2[letter] += 1
    return dictionary1 == dictionary2

print(validAnagram3('','') )
print(validAnagram3('aaz', 'zza'))
print(validAnagram3('anagram', 'nagaram'))   
print(validAnagram3('AnaGram', 'nagaram'))    