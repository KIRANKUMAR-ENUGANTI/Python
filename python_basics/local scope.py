def func():
    a=2
    def funcs():
        nonlocal a
        a+=1
        print(" In funcs {0} scope".format(a))
        print(globals().keys())
        print(locals().keys())
        del a
        try:
            print(a)
        except:
            print("a is deleted in funcs")

    try:
        print(a)
        print("In func scope %d not del yet"%a)
    except:
        print("a is deleted in func scope too")
    funcs()
    try:
        print("In func scope %d"%a)
    except:
        print("a is deleted in func scope too")
func()