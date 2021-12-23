numbers = [3, -10, -4, 1, 9, -12, 8, -3]

positive_nums=[]

for num in numbers:
    if num>0:
        positive_nums.append(num)

print(positive_nums)

#for loop om positieve getallen te vinden
#meer code & meer aantal berekeningen

positive_nums = [num for num in numbers if num>0]
print(positive_nums)
#minder code & minder berekeningen
