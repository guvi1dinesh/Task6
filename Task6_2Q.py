#(2Q) Given python list [10,501,22,37,100,999,87,351]
# count all the prime numbers and create a new python list which will contain all the prime numbers in it:
def primeno(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


lst = [10, 501, 22, 37, 100, 999, 87, 351]
prime = []
count = 0
for num in lst:
    if primeno(num):
        prime.append(num)
        count += 1
print("Total count of prime no:", count)
print("List of prime no:", prime)


#OUTPUT-> Total count of prime no: 1
#         List of prime no: [37]