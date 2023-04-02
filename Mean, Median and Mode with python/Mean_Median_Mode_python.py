# Calculating Mean, Median, Mode in python
import statistics

list = []

n = int(input("Enter the number of elements you want: "))

for i in range(0,n):
    element = int(input())

    list.append(element)
print(f'The list you want is: {list}')

#calculate Mean ()
Sum_List = sum(list)
N_elements = len(list)
Mean = sum(list) / len(list)
print(f'The mean is: {Mean}')

#calculate mode 
print(f'the mode is: {statistics.mode(list)}')

# calculate median
list.sort()
if len(list) % 2 == 0:
    a = list[len(list)//2]
    b = list[len(list)//2 - 1]
    median = (a + b)/2
else:
    median = list[len(list)//2]

print(f'the median is: {median}')



