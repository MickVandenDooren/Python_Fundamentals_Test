var1="String"
var2=float(0.2)
var3=1
var4=True

my_data=[var1,var2,var3,var4]

print('my_data[]=',my_data)

numbers=[]

for x in range(1001):
    if x%2==0:
        numbers.append(x)

print('numbers[]=',numbers)

another_example = [[1.1,1.2],[2.1,2.2]]
print('another_example=', another_example)

another_example.insert(0,[0.1,0.2])
print('inserted an element=', another_example)

another_example.extend([[3.1,3.2]])
print('extended an element=', another_example)