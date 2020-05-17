mytuple=(1,2,3,'c')
print(mytuple)
for i in range(0,len(mytuple)):
    print(mytuple[i])
print(mytuple)
empty_tuple=(1,)
print(empty_tuple)
count=0
for i in range(5):
    empty_tuple=(empty_tuple,)
    print(empty_tuple)
    count+=count
print(count)
a,b,c,d,=mytuple
print(a,b,c,d)
print(mytuple[::-1])
#using tuple function
s="kirankumar"
t=tuple(s)
print("used tuple fun: ",t)
#using a split operator with -1 step to reverse a sting
for i in t[::-1]:
    print(i,end="")
print(t[::-1],end="\n")
#using a tuple with range
tuplefun_withrange=tuple(range(10))
print("tuplefun_withrange:",tuplefun_withrange)

#---------->>tuple can exist without paranthesis
tuple_nopar=1
print("tuple_nopart=1: ",tuple_nopar,type(tuple_nopar))
tup_withpar=('a')
print("tup_withpar=('a'): ",tup_withpar,type(tup_withpar))
'''a tuple with single element is not a tuple unless you have a trailing comma
the type of the tuple gives its datatype calss
single integer--><class 'int'>
single character/string --><class 'str'>'''

# to create a singleton tuple it is necessarty to have a trailing comma
t1=1,
print("type of t1 with single ele and a trailing ,: ",type(t1))
t2=('a',)
print("type of t2 with single ele and a trailing ,: ",type(t2))
# with multiple char or any dataypes always tuple type
t_multi_char='a','b','c'
print(type(t_multi_char))

tuple1=(1,5,3,4,2)
print("len(): ",len(tuple1))
print("sum(): ",sum(tuple1))
print("min max :",min(tuple1),max(tuple1))
new_tuple1=sorted(tuple1,reverse=True)
print("sorted(): ",new_tuple1)
print("reversed(): ",end="")
for i in reversed(new_tuple1):
    print(i,end="")
print()
ext_tup=()
print("different method")
for i in reversed(new_tuple1):
    ext_tup=ext_tup + (i,)
print(ext_tup)
tuple3=("cccc", "b", "dd", "aaa")
print(sorted(tuple3))
print(sorted(tuple3,key=len))
print(sorted(tuple3,reverse=True))
print(sorted(tuple3,key=len,reverse=True))
tupl1=[1,2,3,4]
print(list(zip(tupl1,tupl1)))
a=89
b=89
print(id(a),id(b))
single_ele_tuple=(['a'])
print(type(single_ele_tuple))



print('\n\n\n♥')
#a tuple comprahension returns generatior object
tc=(int(i) for i in range(3))
print(tc)
print(type(tc))
for i in tc:
    print(i)
print(type(1))


singss="kirankumar"
stringg="kiran kumar"
si=tuple(singss)
print(si)
sg=tuple(stringg)
print(sg)

print("id of si is : ",id(si))
si+=sg
print(si)
print("id of si after inplace op: ",id(si))
print()


si=tuple(singss)
sg=tuple(stringg)
print("id of si is : ",id(si))
si=si+sg
print(si)
print("id of si after inplace op: ",id(si))

print('\n\n')

#using empty typle and deleting tuple

tup=tuple()  #tup=()
print(tup)
del tup
print(tup)