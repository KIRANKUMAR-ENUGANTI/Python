a=1
def change_local_a():
    global a
    a=10
    print(a,"is changed in local scope used global keyword")
print(a, " in the global scope")
change_local_a()
print(a," in the global scope")




print()
a=1
def change_local_a():
    a=10
    print(a,"is local changed in local scope no global keyword")
print(a, " in the global scope")
change_local_a()
print(a," in the global scope")
