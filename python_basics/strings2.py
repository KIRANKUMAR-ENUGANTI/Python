s="kiran kumar is a good kiran in the group of kiran"
print(s.center(59,'_'))
print()
print('partition "good": ',s.partition("good"))
print('rpartition "good": ',s.rpartition("good"))
print()
print("prartition 'kiran': ", (s.partition("kiran")))
print("rprartition 'kiran': ", (s.rpartition("kiran")))
print()
print("prartition: 'bad'", (s.partition("bad")))
print("rprartition: 'bad' ", (s.rpartition("bad")))
print()
try:
    print("partition '': ", s.partition(''))
    print("rpartition '': ".s.rpartition(''))
except ValueError:
    print("both exceptions raised ValueError exception")
except:
    print("something went wrong")

s='kiran ia a  ¼ boy'
try: print(s.encode('UTF-8','strict'))
except: print("exception raised")
print(s.encode('UTF-8','replace'))
print(s.encode('UTF-8','ignore'))
print(s.encode('UTF-8','backslash'))
print(s.encode('UTF-8','namereplace'))

str = '12345678910\t12345\ta\tb\t123456789\t\tv'
print(str.expandtabs())
# no argument is passed
# default tabsize is 8
print(str.expandtabs(2))
print()
str_splitlines="123456\rkirankumar is a\tvery good \nboy in the world"
print(str_splitlines)
print("splitlines: ",str_splitlines.splitlines(False))
print("splitlines: ",str_splitlines.splitlines(0))
print("splitlines: ",str_splitlines.splitlines(2))
print("splitlines: ",str_splitlines.splitlines(True))
s="kiran\rkumar\nkirankumar\r\nkirankumar"
print(s)


print()
def fun(item):
    return item.zfill(10)
zfillstring=["-kiran","+kiran","*kiran","%kiran","^kiran"]
print(list(map(fun,zfillstring)))


diff_str='G ë ê k s f ? r G ? e k s'
print(" ascii(): ",ascii(diff_str))
print("bool: ",bool(1))
print("bool: ",bool(s))
print("bool: ",bool(0))
print("bool: ",bool(None))#which gives false
print("bool: ",bool(False))
print("bool: ",bool(True))
print("bytes: ",bytes(b"kian"))


print('\n\n♥')
#using the repr() function
#which is mainly used for debugging
var='kirankumar'
print(repr(var))
var="kirankumar"+' is verygood boy'
print(repr(var))
var=23
print(repr(var))
var=[1,2,3,4]
print(repr(var))
var={1:1,2:2,3:3}
print(repr(var))