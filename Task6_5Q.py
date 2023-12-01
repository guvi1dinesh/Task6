#(5Q) We have to find the difference between the number of mangoes in a bag with maximum mangoes,
# and we have to find bag with minimum mangoes given to the student is minimum

mangoes = [3, 9, 12, 2, 4, 8]     
students = 4

mangoes.sort()          # [2,3,4,8,9,12]
minidif = float('inf')  # the value may come in 2.8,3.9 so that we use float

for i in range(len(mangoes) - students + 1):
    dif = mangoes[i + students - 1] - mangoes[i]
    if dif < minidif:
        minidif = dif

print(minidif)


#Output-> 6
