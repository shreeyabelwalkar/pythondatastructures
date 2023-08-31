sqr = [i*i for i in range(1,11)]
print(sqr)

print([i*i for i in range(1,11)])

numbers = [2,23,56,46,59,569,487,26,12,52,65,58]
odd_numbers = [x for x in numbers if x%2!=0]
print(odd_numbers)
even_numbers = [x for x in numbers if x%2==0]
print(even_numbers)

odd_numbers = [x for x in numbers if x&1]
print(odd_numbers)
even_numbers = [x for x in numbers if x|1]
print(even_numbers)


lst =[(x,y) for x in (1,2,3) for y in (3,1,4) if x!=y]
print(lst)

lst1=[1,3,5,8,-9,8,-7]
newlist = [x*2 for x in lst1]
print(newlist)

pos_list = [x for x in lst1 if x>=0]
print(pos_list)

neg_list = [x for x in lst1 if x<0]
print(neg_list)

new_list = [abs(x) for x in lst1]
print(new_list)

new_list = [pow(x,2) for x in lst1]
print(new_list)

lst =[(x,y,z) for x in (1,2,3) for y in (3,1,4) for z in (5,6,7) if x!=y and y!=z]
print(lst)

lst =[(x,y,z) for x in (1,2,3) for y in (3,1,4) for z in (5,6,7) if x!= y!=z]
print(lst)


animal = ['             camel','cow         ','            horse','           lion']
new_list_animals = [items.strip() for items in animal]
print(new_list_animals)

new_list_=[(x,x*x) for x in range(1,11)]
print(new_list_)

new_list_=[(x,x**2) for x in range(1,11)]
print(new_list_)

lst_=[[1,2,3],[4,5,6],[6,7,8]]
flatten_list = [num for ele in lst_ for num in ele]
print(flatten_list)

from math import pi
new__list =  [round(pi,i) for i in range(1,6)]
print(new__list)

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
transpose = []
for i in range(3):
    transpose.append([row[i] for row in matrix])
print(transpose)

transpose_list = [[row[i] for row in matrix] for i in range(3)]
print(transpose_list)

transpose_list = list(zip(*matrix))
print(transpose_list)
