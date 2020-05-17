print('1♥using while loop')
c=0
while c<4:
    print('in while loop',c)
    c+=1
print('out of while loop')


print()
print('2♥using while loop')
while c>0: print('in while loop',c);c-=1
print('out of while loop')



print()
print('3♥using while loop')
a=[1,2,3,'a','b','kiran']
while a:print('in while loop',a.pop())
print('out of loop')




print()
print('4♥using while loop')
while c<5:
    print('in while loop',c)
    c+=1
else:
    print('in esle since the value of c is 5')



print()
print('5♥using while loop')
while c>0:print('in while loop',c);c-=1
else:print('in else shice the value of c is 0')



print()
print('6♥using while loop')
while c<5:
    print('in while block',c)
    if c==4:
        print('the value of c is 4,\nconditon will false if its increased \nso we should break here')
        break
    c+=1



print()
print('7♥using while loop')
c=3
d=3
while c>0:
    print('whiel1',c)
    while d>0:
        print('whiel2',d)
        d-=1
    else: print('out of while2',d);d=3
    c-=1
else: print('out of while1',c)



print()
print('8♥using while loop')
c=3
d=3
while c>0:
    print('whiel1',c)
    while d>0:
        print('whiel2',d)
        d-=1
        if d == 2: break
    else: print('out of while2',d);d=3
    c-=1
else: print('out of while1',c)


print()
print('9♥using while loop')
c=3
d=3
while c>0:
    print('whiel1',c)
    while d>0:
        print('whiel2',d)
        d-=1
        if d==2:continue
        print(d)

    else: print('out of while2',d);d=3
    c-=1
else: print('out of while1',c)



print()
print('10♥using while loop')
c=3
d=3
while c>0:
    print('whiel1',c)
    while d>0:
        print('whiel2',d)
        d-=1
        if d==2:pass
        print(d)

    else: print('out of while2',d);d=3
    c-=1
else: print('out of while1',c)


