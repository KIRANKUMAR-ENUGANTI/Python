
def conter():
    num = 0

    def incrementer():
        nonlocal num
        num+=1
        print("num in the incrementer:%d"%num)
        num+=1
        print("num IN THE INCREMENTER:%d"%num)

    print("num in the counter : %d"%num)
    incrementer()
    num+=1
    print("in the counter : %d"%num)
conter()


print('\n\n\n♥')
#without using nonlocal keyword

def conter1():
    num = 0

    def incrementer1():
        num=0
        num+=1
        print("num in the incrementer:%d"%num)
        num+=1
        print("num IN THE INCREMENTER:%d"%num)

    print("num in the counter : %d"%num)
    incrementer1()
    num+=1
    print("in the counter : %d"%num)
conter1()


