# (7Q) Write a python program to find the first non - repeating element in the given list of integer:

def non_repeating_element(nre):
    count = {}
    for number in nre:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    for number in nre:
        if count[number] == 1:
            return number
    return None


nre = [22, 23, 19, 22, 23, 14, 18, 48, 39]

result = non_repeating_element(nre)
if result is not None:
    print("Non-repeating element is:", result)
else:
    print("No non-repeating element")



#Output-> Non-repeating element is: 19


# #Definition: why is printing 19 mean,
# In the list which non-repeat number comes first that single No only taken as output
