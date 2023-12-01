# (9Q) you have given a python list [10,20,30,9] and a value of 59.
# write a python program to find the triplet in the list whose sum is equal to the given value

def triplet(lst, target):
    n = len(lst)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if lst[i] + lst[j] + lst[k] == target:
                    return [lst[i], lst[j], lst[k]]
    return


lst = [10, 20, 30, 9]
target = 59
triplet = triplet(lst, target)

if triplet:
    print(f"Exact original value",triplet)
else:
    print("Not a original value")



#Output-> Exact original value [20, 30, 9]

#Definition:we have to find the original value 59 ,in the list we have to add each for eg:20+30+9=59,
#then we are matching original value 59 and list value 59,the condition satisfies value of 59