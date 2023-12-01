#(4Q) Write a python program to find the sum of the first and last digit of an integer:

num = 1998
firstdigit = int(str(num)[0])
print(f"Firstdigit:",firstdigit)

lastdigit = num % 10
print(f"Lastdigit:",lastdigit)

sum = firstdigit + lastdigit

print(f"Sum of first and last digit:", sum)


#Output-> Firstdigit: 1
#         Lastdigit: 8
#         Sum of first and last digit: 9

