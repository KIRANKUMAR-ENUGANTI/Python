mylist=[1,2,3]
print(mylist)



print('\n\n\n  1♥')
print('APPEND METHOD')
mylist.append(4)
print('ap sigle ele 4 to mylist: ',mylist)

print()
mylist.append([4])
print('ap another list with single ele  [4] to mylist: ',mylist)

print()
mylist.append([3,2,1])
print("app another list [3,2,1] to my list:",mylist)

print()
print("accesing the ele mul-dimen list mylist[5][2]: ",mylist[5][2])

print()
mylist[5].append(126)
print("app ele in multi-dim list 126 in mylist[5] : ",mylist)

print("accesing the ele mul-dimen list af app mylist[5][3] : ",mylist[5][3])



print('\n\n\n2♥')
#diff append and extend
mylist_app=[1,2,3]
mylist_extnd=[1,2,3]

print("bef anything: and the len of mylist_app: ",mylist_app,len(mylist_app))
print("bef anything: and the len of mylist_extnd: ",mylist_extnd,len(mylist_extnd))

print()
mylist_app.append([4,5])
print("af appe [4,5]: and len of app mylis_app: ",mylist_app,len(mylist_app))

print()
mylist_extnd.extend([4,5])
print("af ext [4,5]: and len of ext mylist_extnd: ",mylist_extnd,len(mylist_extnd))

print()
mylist_app.append([6])
print("app [6] it takes new list as ele: ",mylist_app,len(mylist_app))

print()
mylist_extnd.extend([6])
print("extnd [6] it consider as single lis ele: ",mylist_extnd,len(mylist_extnd))



print('\n\n\n4♥')
# usng isert method
mylist_ins=[1,2,3,4]
mylist_ins.insert(0,['a','b','c'])
print('ins list [a,b,c] at 0 index in mylist_ins: ',mylist_ins)


print('\n\n\n5♥')
#using index method
mylist_indx=[1,2,3,3,4,5,3]
print('indx of 3 in mylist_indx: ',mylist_indx.index(3))

print()
print('index of 3 b/n 0-4: ',mylist_indx.index(3,0,4))

print()
print('index of 3 b/n 0-3: ',mylist_indx.index(3,0,3))

print()
print('index of 3 b/n 2-6: ',mylist_indx.index(3,2,6))

print()
#using count method which takes exactly one parameter
print('cout of 3 is : ',mylist_indx.count(3))
print('cout of 3 is : ',mylist_indx.count(2))


print('\n\n\n6♥')
#using pop method
mylist_pop=[1,2,3,4]
popedlis_ele=mylist_pop.pop()
print("the ele at last(default if no para mentioned) is poped and returned: ",popedlis_ele)
print('pop is an inplace method effected myllist_pop',mylist_pop)

print()
popedlis_ele=mylist_pop.pop(0)
print("the ele at 0(mentioned para) is poped and returned: ",popedlis_ele)
print('since its a inplace op: ',mylist_pop)



print('\n\n\n7♥')
#using remove
mylist_r=[1,2,2,2,3,2,4]
print('list before remove op: ',mylist_r)
mylist_r.remove(2)
print('removed 2 list is changed sicne it an inplac op : ',mylist_r)
print()
#using del keyword to del slice
del mylist_r[1:3]
print('del slice of list [1:3] i.e; [2,2]',mylist_r)


print()
#using reverse method
mylist_r.reverse()
print('.reverse() the list eles: ',mylist_r)

print()
#using clear method
mylist_r.clear()
print('list is cleared now its empyt: ',mylist_r)


print('\n\n\n8♥')
#using   copy method
print('used assignment')
mylist_c=[1,2,3,4,5]
mylist_b=mylist_c
print('c,b: ',mylist_c,mylist_b)
print("the id of c and b are: ",id(mylist_c),id(mylist_b))
mylist_c.append(6)
print("c appended wiht 6 then b is affected: ",mylist_c,mylist_b)

print()
print('to avoid use slice')
print('c,b: ',mylist_c,mylist_b)
mylist_b=mylist_c[:]
print("the id of c and b are : ",id(mylist_c),id(mylist_b))
mylist_c.append(60)
print("c appended with 60 b is not affected: ",mylist_c,mylist_b)

print()
print('to avoid use list fun')
print('c,b: ',mylist_c,mylist_b)
mylist_b=list(mylist_c)
print("the id of c and b are: ",id(mylist_c),id(mylist_b))
mylist_c.append(600)
print("c appended with 600 b is not affected: ",mylist_c,mylist_b)



print('\n\n\n9♥')
#using sort fun
l=["cccc", "b", "dd", "aaa"]
print("actual list is: ",l,id(l))
print("sorted l is: ",l.sort(),'it will return None because we cannot print cz action not yet completed')
l.sort()
print("sorted l is: ",l,id(l))
print("l is sorted using sort() so, l[0] is: ",l[0])
print('because its a inplace operator which directly affect the list')
l.sort(key=len)
print("l.sort() with key: ",l,id(l))
l.sort(reverse=True)
print('l.sort() with reverse: ',l,id(l))
print('becz it first sort lexographically then reverses it. so, you need you use both key and reverse to get it')
l.sort(key=len,reverse=True)
print('l.sort() with both key and reverse: ',l,id(l))
print()
print('assign and check id')
j=l.sort()
print(j,id(j),id(l))
print('cause sort desnot return anything')

print()
####we can also use the bultin sorted function
l=["cccc", "b", "dd", "aaa"]
print("actual list is: ",l)
print("sorted l is: ",sorted(l))
print("l is sorted using sorted() so, l[0] is: ",l[0],'not an inplace operator')
print(sorted(l,key=len))
print(sorted(l,reverse=True))
print(sorted(l,key=len,reverse=True))
print()
k=sorted(l)
print(k,id(k),id(l))


print('\nhow sort fun works')
############how the sort and sorted fun works
k=['c','d','a','b']
print("actual list k is: ",k)
print('sorted k using sorted() is: ',sorted(k))
print("k is sorted using sorted() so,k[0] is",k[0])
k.sort()
print("sorted k using sort() is: ",k)
print("k is sorted using sort() so,k[0] is",k[0])


print()
print('list of lists')
sorted_list1=[[1,2],[5,6],[5,3],[6,1]]
print(sorted(sorted_list1))
sorted_list1.sort(reverse=True)
print(sorted_list1)
sorted_list1.reverse()
print(sorted_list1)

print()
print('how to sort nestd list')
nsl=list()
[nsl.append([i,j]) for i,j in zip(range(5),range(5,0,-1))]
print(nsl)
nsl=sorted(nsl,key=lambda x:x[1])
print('sorted list based on the secon element in each nested list',nsl)
print()
nsl=sorted(nsl,key=lambda x:x[0])
print('sorted list based on the first element in each nested list',nsl)


print('\n\n\n10♥')
#####list concat and zip
list_one=[1,2,3]
list_two=[4,5,6]
print('list_one,list_two: ',list_one,list_two)
mergerdlist=list_one+list_two
print(" the concated list is: ",mergerdlist)

print('\nusing zip fun')
## using zip
for a ,b in zip(list_one,list_two):
    print(a,b)
print(list(zip(list_one,list_two)))
list_dup=[1,5,2,3,2,4]
print(list_dup,"before removeing dup")
print(set(list_dup),"after remove dup by using set method")



print('\n\n\n11♥')
####nested list using list compherension
a=[[0 for y in range(5)] for x in range(4)]#[[0,0,0,0] for x in range(4)]
print(a)
nlist=[[0,0,1],[1,0,0],[0,1,0]]
for i in nlist:
    print(i)
c=0
print([x for y in nlist for x in y])
my_list=[ _ for _ in range(10) if _ != 2]
print(my_list)

print('\n\n\n12♥')
#using replication
my_list1 = [None] * 10
my_list2 = ['test'] * 10
print(my_list1)
print(my_list2)

my_list =[1,2,3]
my_list=my_list *2
print(my_list[2])


#you can use direct index on the original list to access the eleentw
print([1,2,3,4][2])






