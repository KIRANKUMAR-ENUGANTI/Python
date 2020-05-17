# their should be 1.positional   2.default   3.keyword    4.*args   5**kwargs





def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def curse(strings):
    return f'{strings}you mother fucker'
def operation(fun,*args):
    c=fun(*args)
    return c
#calling opertion required
print(operation(add,2,3))
print(operation(mul,2,3))
print(operation(curse,'curse'))


print('\n\n\n♥')
# a fun 'F' which is in local scope of 'A' called form outside 'A'
#jus return that fun 'F' in 'A' and assign it to a var
#now call that var
def crete_pow():
    def pow(y):
        return y*y
    return pow
ad=crete_pow()
print(ad(5))




def crete_pow2(x):
    def pow2(y):
        return y**y
    return pow2
    
x=100
ad=crete_pow2(x)
print(ad(5))
ad=crete_pow2(x)
print(ad(5))


print(type(type(7)))
print('\n\n\n♥')
#keywod arguments
def a(age,name):
    return f'hi {name} and you are already {age}'
print(a(age=21,name='kirankumar'))
print(a(name='sreya',age=20))
print(a(21,name='kiran'))

# print(a(age=21,"kiran"))
# RAISE AN ERROR POSITIONAL ARG AFTER KEYWORD ARG
# print('kiran',age=21)
#kiran is assigned to age already now again defining age become invalid


print('\n\n\n♥')
# #using packing and unpaccking tuple and list as arbitary arg
def addition(b,*a):
    k=0
    for i in a:
        k=k+i
    return k
l=[1,2,3,4,5]
# print(addition([1,2,3,4,5]))
#we cannot send a list directly instead
print(addition(1,2,3,4,5))
#send the tuple elements
print(addition(*l))


def af(a=[]):
    for i in a:
        a.append(i)
    return a
a=[1,2,3,4,5]
print(af([1,2,3,4,5]))