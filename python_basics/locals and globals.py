print('1♥')
a=1
b=2
c=3
def fun1():
    global a
    a=21
    b=1
    s="kiran"
    print()
    print("fun1: ",locals())
    print()

    print("fun1: ",globals())
    print()

def fun2():
    global c
    c=32
    str="kumar"
    string="kuran"
    aa=1
    bb=2
    print()

    print("fun2: ",locals())
    print()

    print("fun2: ",globals())
    print()

fun1()
fun2()




print('n\n\n2♥')
s ="im fine and fuck you"
def func():
    global s
    print(s)
    s="damm fuck you"
    print("s changed by func {}".format(s))
    del s
    try:
        print(s)
    except:
        print(" s is deleted in this funceion")

print(s)
func()
try:
    print(s)
except:
    print("s is already deleted globally")


print(globals().keys())
print(locals().keys())