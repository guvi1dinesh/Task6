#(10Q) Given a list[4,2,-3,1,6]
# write a python program to find if there is a sub-list with sum equal to zero


def sublist(slz):
    sub1 = set()
    sub2 = 0
    for num in slz:
        sub2 += num
        if sub2 == 0 or sub2 in sub1:
            return True
        sub1.add(sub2)
    return False
slz = [4, 2, -3, 1, 6]

if sublist(slz):
    print("Sublist with sum equal to zero")
else:
    print("Sublist with sum not equal to zero")


#Output-> Sublist with sum equal to zero


## Definition: in a list we are adding two numbers eg:2+1=3,In list other number as value (-3)
# Then we are subtracting 3-3 =0 ,Final we find the sublist is equal to zero.

