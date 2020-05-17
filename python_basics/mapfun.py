def add(a):
    return a+a
def mul(c,d):
    return c*d
n=[1,2,3,4]
m=(1,2,3,4)
r=map(add,n)
print("only one iter: ",list(r))
r=map(mul,n,m)
print("two diff iter: ",list(r))
# if iter are of diff len then the map fun stops mapping
#untill the shorter iter exhausted
x = map(lambda e : e.upper(), ['one', 'two', 'three', 'four'])
print(list(x))

y=map(int,input().split())
print(list(y))

y=map(lambda n:int(n),input().split())
print(list(y))