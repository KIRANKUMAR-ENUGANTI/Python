s="0000111"
print(s)
c=int(s,2)
print(c,"convertd string 0000111 into base 2")
c=float(s)
print(c)
c=hex(16)
print(c)
c=oct(8)
print(c)
s="a"
c=ord(s)
print(c)
x='KiranKumar'
y=b'KiranKumar'
d=x.encode('ASCII')
if d==y:
    print("same")
else:
    print("not same")

print((d,y))
virgin=True
bitch=False
print("fuck you" )if virgin else print("get fucked")
