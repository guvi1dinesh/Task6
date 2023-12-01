#(3Q)Given apython list [10,501,22,37,100,999,87,351]
# Find how many numbers are there in the given python list which are Happy Numbers

def happy_number1(n):
    base = set()
    while n != 1 and n not in base:
        base.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))     #calculating value of list numbers
    return n == 1                                        #finaly checking n ==1 or not,if 1==1 happy number is found
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
happy_numbers = 0
for number in list1:
    if happy_number1(number):
        happy_numbers += 1
print("No of Happy Numbers:", happy_numbers)


#Output-> No of Happy Numbers: 2



