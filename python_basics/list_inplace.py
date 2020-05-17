"""li=[1,2,3,4]
print("li and id is: ",li,id(li))
lis=li
print("lis and id is: ",lis,id(lis))
li=li+[5,6,7]
print("af normal add li and id is: ",li,id(li))
print("af normal add lis and id is: ",lis,id(lis))
"""
li=[1,2,3,4]
print("li and id is: ",li,id(li))
lis=li
print("lis and id is: ",lis,id(lis))
li+=[5,6,7]
print("af normal add li and id is: ",li,id(li))
print("af normal add lis and id is: ",lis,id(lis))

# NOTE: since list is mutabe but for immuable it works diff