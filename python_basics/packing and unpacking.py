print('1♥')
def fun(*c):
    a=[*c]  #*c packed the indv args into list so c itself is a list   ,a=c
#a=c correct
    for i in range(0,len(a)):
        print(a[i])
    # print(a[0], a[1], a[2], a[3])


a=["1","2","3","4"]
fun(*a)
fun(1,2,3,4)

print('\n\n\n2♥')
def fun1(*c):  # packing the indv args to a singe arg c itslf is a tuple
    a=(*c,)  #we can also use directly c since itself a tuple  , a=c
    x,y,z,k=a
    print(x,y,z,k)
    for i in range(0,len(a)):
        print(a[i])
    # print(a[0],a[1],a[2],a[3])
a1=("1","2","3","4")
fun1(*a1)
fun1(5,6,7,8)# unpacking the tuple to its args indv




print('\n\n\n3♥')
import keyword
def func(**arg_are_keywords):
    dicti=arg_are_keywords#{**arg_are_keywords}
    for k in dicti:
        print(keyword.iskeyword(dicti[k]))
    for key in arg_are_keywords:#we can direlctly use it the formal parameter
        print(key,":",arg_are_keywords[key])
        print(keyword.iskeyword(arg_are_keywords[key]))

keywords = {'1':'def','2':'in','3':'with','4':"print",'5':"alice"}

func(**keywords)  #unpcking the dict arguments to indiidual




print('\n\n\n4♥')
#why it is printing list
*a,=(1,2,3)
print(a,type(a))


print('\n\n\n5♥')
#using *args and *kwargs
def fun3(*l,**k):
    print('for k or **kwargs')
    for i in k:
        print(i,k[i])
    print('for l or *args')
    for p in l:
        print(p)



c=[1,2,3]
fun3(1,2,3,4)
fun3(*c)
fun3(b=2,name='kiran',age='21',gender='M')
d={'u':2,'name':'sreya','relation':'lover','kiss':'yes'}
fun3(**d)
print('\n\n')
fun3(*c,**d)

