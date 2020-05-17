# we have list comprahension
l_c=[x for x in range(5)]
print(l_c)
for i in l_c:
    print(i)
for j in l_c:
    print(j)
l=set(l_c)
print(l)
print('\n\n')
l_c=[x**2 for x in l_c]
l_c.extend([4,4,4,1,1,1,9,9,9])
print(l_c)


print('\n\n')
# we have set comprahension
s_c={int(x**(1/2)) for x in l_c}
print(s_c)
for i in s_c:
    print(i)
for j in s_c:
    print(j)
l=list(s_c)
print(l)
print('\n\n')
# we have 0dict comprahension
d_c={ k:v for (k,v) in zip(list(s_c),list(s_c))}
print(d_c)
for i in d_c:
    print(i)
for j in d_c:
    print(j)
l=list(d_c)
print(l)



print('\n\n♥♥♥♥')
#Generators are kind of comprahensions with paranthesis
#and they are once utilized need to generate again
expression = (x for x in range(10))
print(expression)# jus returned the obj instead printing the entire body
#unlike other comprahensions
for i in expression:#here we utilized generator by iterating the obj
    print(i)
g=list(expression)#the expression has nothing since we have already utilized above
print(g)#this prints empty list since expression is empty converted to list



print('we can use the generator fun without paranthesis in some builtin funlike sum max min...')
print(sum(x for x in range(10)))
print(max(x for x in range(10)))
print(min(x for x in range(10)))
