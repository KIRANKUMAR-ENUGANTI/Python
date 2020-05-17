print('1♥')
#using lists
x=[1,2,3]
y=x
z=[1,2,3]
if x is y:print(id(x),id(y))
if x is  z: print(id(x),id(z))
if y is  z: print(id(y),id(z))
y.append(4)
print(x)

x=[1,2,3]
y=x[:]
z=[1,2,3]
if x is y:print(id(x),id(y))
if x is  z: print(id(x),id(z))
if y is  z: print(id(y),id(z))
y.append(4)
print(x)




print('\n\n\n2♥')
#using dictionary
x={1:1,2:2}
y=x
z={1:1,2:2}
if x is y:print(id(x),id(y))
if x is  z: print(id(x),id(z))
if y is z: print(id(y),id(z))
y.update([(3,3)])
print(x)


print('\n\n\n2♥')
#using set
x={1,2,3}
y=x
z={1,2,3}
if x is y:print(id(x),id(y))
if x is  z: print(id(x),id(z))
if y is z: print(id(y),id(z))
y.add(4)
print(x)


print('\n\n\n2♥')
#using tuple
x=(1,2,3)
y=x
z=(1,2,3)
if x is y:print(id(x),id(y))
if x is  z: print(id(x),id(z))
if y is z: print(id(y),id(z))




print('\n\n\n2♥')
#using int
x=1
y=x
z=1
if x is y:print(id(x),id(y))
if x is  z: print(id(x),id(z))
if y is z: print(id(y),id(z))



print('\n\n\n2♥')
#using int
x='kiran'
y=x
z='kiran'
if x is y:print(id(x),id(y))
if x is  z: print(id(x),id(z))
if y is z: print(id(y),id(z))