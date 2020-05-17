'''True and x is x
    False or x is x
drawback: ontrue the x must not be 0 or false
if itis the onfalse will be executed always

we also have
True or x is True
False and x is False
'''


a,b=0,1
x,y=1111111111,999999999
print('\n1♥')
print(a<b and False or "hai")#always prints hai cause on_True is false
print("x and False =False\
      False or y =y")


print('\n2♥')
min =(x,y)[a<b]
print('used tuple ele for ontrue and onfalse of exp: ',min)
print('used lambdas which jus return values inside a tuple '
      'for ontrue and onfalse  fo exp',
    (lambda :x,lambda : y) [a<b]()  )


print('\n3♥')
min={True:a,False:b} [a>b]
print('used dict elements for ontrue and onflase of exp: ',min)



print('\n4♥')
str="hai" if 2==3 else "hello"
print('used jus ternary operator: ',str)

str="hai" if 2==3 else "hello" if 1==2 else "bollo"
print('used ternary op inside ternary op: ',str)



print('\n5♥')
print('1')
print("" and "hello")
print("" is False)
print(2)
print("" or "hello")
print(3)
print(0 and False)

