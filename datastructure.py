lst=[1,2,78,78,4,78,5,6,78]
print(lst)

lst.append(30)
print(lst)

lst1=[4,55,65,78,25]
lst.append(lst1)
print(lst)
print(lst[3])

lst2=lst.copy()
print(lst2)

cnt = lst.count(6)
print('cnt=',cnt)

lst3=[55,56,78]
lst.extend(lst3)
print(lst)

n = lst.index(78)
print('index of 78=',n)

n = lst.index(78,4)
x= lst.index(78,n+1)
print('index of 78=',x)

lst.pop()
print(lst)

lst.pop(3)
print(lst)

lst.remove(30)
print(lst)

list = [1,2,3,5,6,7]
list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.clear()
print(list)

