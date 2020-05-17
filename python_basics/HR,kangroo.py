#both kangroo should land at same position at same number of jumps
def kangaroo(x1, v1, x2, v2):                       
    str="NO"
    if (0<=x1<x2<=10000 and 1<=v2<v1<=10000) or \
            (0<=x1>x2<=10000 and 1<=v2>v1<=10000):
           for i in range(1000):
               x1=x1+v1
               x2=x2+v2
               if x2==x1:return "YES"
           else: return str
    else:return str

b=[int(a) for a in  input().split()]
x1, v1, x2, v2=b
result = kangaroo(x1, v1, x2, v2)
print(result)