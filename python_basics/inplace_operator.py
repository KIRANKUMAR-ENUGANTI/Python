import operator
x="hai"
y="hello"
x=operator.iadd(x,y);
print(x)
y="kiran"
z="kumar"
y=operator.iconcat(y,z);
print(y)
y="kirankiran"
y+=z
print(y)



print('\n\n\n♥')
li=[5,4,3,2,1]
print('li: ',li)
li2=li
print('ids are same after assign') if li is li2 else print("not same after assing")
li2.append(0)
print('ids are same after append of li2') if li is li2 else print("not same after append ")
print('li2: ',li2)
print('li ele are also changed since both ids are same')
print('li: ',li)


print('\n\n\n♥')
print("normal addition of lists\n")
li=li+[1,2,3,4]
print('ids are same after li normal add') if li is li2 else print("ids are not same after li normal add new li is created ")
print('li: ',li)
print('after li update this is a new li')
print('li2',li2)
print('li2 ele are unchanged since this is same as old li not new li')



print('\n\n\n♥')
print('inplace addition')
list1=[1,2,3]
print('list1: ',list1)
list2=list1
print('list2',list2)
print('ids are same') if list1 is list2 else print("ids are not same ")

list1+=[1,2,3,4]
print('ids are same') if list1 is list2 else print("ids are not same ")

print('list1: ',list1)
print('list2',list2)
