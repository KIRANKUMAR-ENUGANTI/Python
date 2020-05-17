print('1♥')
print('using set() method')
s=set()
s_raw=set()
print("blank set and its type; ",s,type(s))
strings="kirankumar"
print("string to set: ",strings,set(strings))#WHY the ORDER FOR THE ELEMTNTS keep changing everytime
print()
s1=[1,2,3,3,3,3,4,4,5,1]
s2=list(strings)
print('list of numbers to set: ',s1,set(s1))#why their is no shuch weired order for the elements in for a list converted to set
print('list of strings to set: ',s2,set(s2))

print()
t1=tuple(s1)
print('tuple of numbers to set: ',t1,set(t1))
t2=tuple(s2)
print('tuple of strings to set: ',t2,set(t2))
print()
sd={1:10,2:20,3:30}
print('dict to set: ',sd,set(sd))
s_diff_dtyps=[0,1,2,3,'q','w','e','kiran',True,False,None,(1,2,3)]
print("s_diff_hashable/immutables to set: ",set(s_diff_dtyps))
#using raw ds
print('sraw: ',set('kiran'))
print('sraw: ',set((1,2,4)))
print('sraw: ',set([1,2,4]))
print('sraw: ',set({1:0,2:0,4:0}))





print('\n\n\n2♥')
print('using add method ')
sa={1,2,3,4}
print('set ready for addition: ',sa)
sa.add(5)
print('sa added with single int ele: ',sa)
sa.add('kiran')
print('sa added with string : ',sa)
sa.add((1,2,3))
print('sa added with tuple : ',sa)
print()

try:
    sa.add(sa)
except:
    print('raised a TypeError unhashable SET so did not affected the origial set: ', sa)

print()
try:
    sa.add([1, 2, 3])
except:
    print('raised a TypeError unhashable  LIST so did not affected the origial set: ', sa)

print()
d={k:v for (k,v) in zip(range(5),range(5,0,-1))}

try:
    sa.add(d)
except:
    print('raised a TypeError unhashable  DICT so did not affected the origial set: ', sa)


print('when you try to add a set with immutable or unhashable '
      'you endup with TypeError: unhashabl type: list or set or dict'
      'ele  must be a single immutable object')

print('final set is unchanged for list or set or dict addition: ',sa)





print('\n\n\n3♥')
print('using update method')
su={1,2,3}
su1={4,5,6}
su.update(su1)
print('update set with another set elements: ',su)
lu=[6,7,8,]
su.update(lu)
print('updateing a set with a list  elements: ',su)
lu=[4,5,6,(7,8,9)]
su.update(lu)
print('updateing a set with a list elements containing tuples elements: ',su)


print()
tt=tuple(lu)
print('tt:',tt)
su=set()
print('set: ',su)
su.update(tt)
print('updateing a set wit a tuple elements : ',su)
su.update((1,2))
print('updateing a set wit a direct tuple elements: ',su)
su.update('s')
print('updateing a set wit a single elements: ',su)
print()
print('a dictionary s_diff_dtyps: ',s_diff_dtyps)
su.update(s_diff_dtyps)
print('update set wth s_diff_dtyps:',su)

print('final set is : ',su)





print('\n\n\n4♥')
print('using remove and discard')
print("set we have: sa ",sa)
#remove returns nothing
removed_ele=sa.remove('kiran')
print('removing "kiran" from sa',removed_ele)
print('set: ',sa)
sa.add('kiran')
print('added kiran back after removed by remove method',sa)
print('removing "kiran" from sa',sa.remove('kiran'))

sa.add('kiran')
print('added kiran back after removed by remove method',sa)
discarded_ele=sa.discard('kiran')
print('discarding "kiran" from sa',discarded_ele)

sa.add('kiran')
print('added kiran back after removed by remove method',sa)
print('discarding "kiran" from sa',sa.discard('kiran'))

print('\n\nwith non exted ele')
print('set: ',sa)
try:
    print('removing  from sa', sa.remove('kumar'))
    print('thoug non exted ill print,remove')
except:
    print('raised exception for non existed remove(kumar)')
print('set: ',sa)
try:
    print('discarding  from sa', sa.discard('kumar'))
    print('thoug ele not found nothing happens,discard')
except:
    print('raised exception for non existed discard(kumar)')


print('\n\nwith no ele')
print('set: ',sa)
try:
    print('removing  from sa', sa.remove())
except:
    print('raised exception for remove()')
print('set: ',sa)
try:
    print('discarding  from sa', sa.discard())
except:
    print('raised exception for discard()')
print('set: ',sa)




print('\n\n\n5♥')
print('using pop method')
print('set: ',sa)
sa.pop()
print('pop the first ele by default: ',sa)
poped_ele=sa.pop()
print('pop returned the poped ele: ',poped_ele)
print('now the set is: ',sa)
print('pop in print:',sa.pop())
print('set: ',sa)
print('pop in print:',sa.pop())
print('set: ',sa)
print('pop in print:',sa.pop())
print('set: ',sa)
se=set()
try:
    print(se.pop())
except:
    print('reaised an exception cuz no ele to pop set is empty')
print('set: ',se)

se.update('k','i','r','k','i','r')
print('se set ele are: ',se)




print('\n\n\n6♥')
print('using clear method')
se.update('kirankumar')
print('se set ele are: ',se)
se.clear()
print(se)





print('\n\n\n7♥')
print('using FROZENSETS:')
print('NOTE: no modifying ops like add pop clear..')
sf=set('kirankumar')
print('set sf: ',sf)
se.update('kiran')
print('set se:',se)
fset=frozenset(sf)

#using a modifying method to test
print('fset and id before &=: ',fset, id(fset))
fset=fset&se
print('fset and id before &=:',fset,id(fset))
se.clear()
print('set se: ',se)
try:
    se.update({1,2,3,{44,55},{123,321}})
except:
    print("reaised an exception since sets are immutable")

try:
    se.update({1,2,3,frozenset({44,55}),frozenset({123,321})})
except:
    print("reaised an exception since sets are immutable")
print(se)




print('\n\n\n8♥')
print('mathematical operations')
s1={1,2,3}
s2={2,3,4}
sresult=s1.intersection(s2)
print('intersection sresult: ',sresult)
print('&: ',s1&s2)

print()
sresult=s1.union(s2)
print('union sresult: ',sresult)
print('|: ',s1|s2)


print()
sresult=s1.difference(s2)
print('difference sresult: ',sresult)
print('-: ',s1-s2)


print()
sresult=s1.symmetric_difference(s2)
print('symmetric_difference sresult: ',sresult)
print('^: ',s1^s2)

print()
print('changed ele of s1 and s2')
s1={1,2,3}
s2={2,3,4,1,5}
sresult=s1.issubset(s2)
print('issubset sresult: ',sresult)



print()
sresult=s2.issuperset(s1)
print('issuperset sresult: ',sresult)



print()
s1={1,2,3,4,6}
s2={4,6,5,7}
sresult=s1.isdisjoint(s2)
print('isdisjoint sresult: ',sresult)


print('\n\n')
print('set s1: ',s1)
print('set s2: ',s2)


print('inplace ops')
s1|=s2
print('union(union_updae): ',s1,s2)

print()
s1-=s2
print('difference_updae: ',s1,s2)

print()
s1^=s2
print('symmetric_difference_updae: ',s1,s2)

print()
s1&=s2
print('intersection_update: ',s1,s2)
