mylist= [1,2,3,4,5,6,7,8,9,10]
new_list =[]

def isDivisible(thelist):
    for i in mylist:
        if i % 2 == 0:
             new_list.append(i)
    print(new_list)    
isDivisible(mylist)