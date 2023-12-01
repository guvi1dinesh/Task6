#(6Q)You have been given three lists.find the duplicates in the three lists.write a python program for the same:

list1 = [23, 22, 40, 48, 69, 75, 60]
list2 = [48, 15, 60, 75, 18]
list3 = [69, 60, 48, 98]
set1 = set(list1)                    #list is converted to set to find dulplictes values
set2 = set(list2)
set3 = set(list3)

result1 = set1.intersection(set2, set3)
Finalresult = list(result1)
print("Duplicates in the three lists:", Finalresult)


#Output-> Duplicates in the three lists: [48, 60]





