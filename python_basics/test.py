d={x:y for (x,y) in zip(range(2,5),range(4,7))}
print(d)
print('poped last item: ',d.popitem())
print(d)
d[1]=1
print(d)
print(dict(sorted(d.items(), key =lambda i:  (i[1],i[0]))))
print('poped last item: ',d.popitem())

d1=dict(sorted(d.items(), key =lambda i:  (i[1],i[0])))
print('poped last item: ',d1.popitem())

import random
print('\n')
rad_l1=[]
for i in range(3):rad_l1.append(random.randint(0,10))
rad_l2=[]
for i in range(4):rad_l2.append(random.randint(0,10))
print('using key parameter in sort fun for lists')
l=[[(x+k) for x in rad_l1] for k in rad_l2]
print(l)
l.sort(key=lambda x:x[2])
print('sort on the third list of list ele: ',l)


a,b,_,_=1,2,3,4
print(a,b,_)
list=[1,2,3]
f=[1,2,3]
print(list)
try:
    print(list(l))
except:
    print("is a error, bcz list is used as a variable name. \nso, cannot use it as a convertion function \nits been overrided")
print('special case: \n though int is a key in dict its actual \nfunctionality is not been overrided')
d={int:2}
print(d[int])
j=int('8')
print('its working: ',j)
int=23
print('int: ',int)
try:
    j = int('0')
    print(j)
except:
    print('its a error cuz,\n int is used as var name its functionality is been overrided \nwe cannot use it for convertions')

set=3
float=3
tuple=3
dict=4
str=89
bool=99
print('same thing happend with'
      'set,float,tuple,dict,str,bool: ')
print(set,float,tuple,dict,str,bool)
print('Note: anyway we cnnot ue directly keywords like True,False,None ... as variables names')
