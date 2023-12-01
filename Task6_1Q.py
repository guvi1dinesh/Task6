#(1Q) python program using list [10,501,22,37,100,999,87,351]
# create two list one which have all the even numbers and another list which have all the odd numbers in it

numbers = [10,501,22,37,100,999,87,351]

even =[num for num in numbers if num % 2 == 0]
print(f"even number:{even}")                            #o/p-> even number:[10, 22, 100]

odd =[num for num in numbers if num % 2 != 0]
print(f"odd number:{odd}")                              #o/p-> odd number:[501, 37, 999, 87, 351]
