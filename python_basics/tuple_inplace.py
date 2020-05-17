# tuples are immputable
tup_inplace=(1,2,3,4,5)
print("tup_inplace: ",tup_inplace)
print("id tup_inplace: ",id(tup_inplace))
q=tup_inplace
print("id of q: ",id(q))
print("q=tup_inplace: ",q)
tup_inplace+=(6,7,8,9)
print("after inplace: ",tup_inplace)
print("id of tup_inplace af inplace: ",id(tup_inplace))
print("q=tup_inplace: ",q)
s="kirankumar"
tup=tuple(s)
print(tup)
print(tup[:])
print(tup[1:])#from index 1 to end
print(tup[::-1])#reverse of a stirng
print(tup[:-1])#from start to 9(10-1)
print(tup[-1:])#from last to end sequence

print(tup[1:5:2])
print(tup[::-1])





