print('1♥')
#####Changing The Capitalization Of A String
name="thE Geek leTTer iS: ß"
print("casefold: ",name.casefold())
print("upper: ",name.upper())
print("lower: ",name.lower())
print("capitalize: ",name.capitalize())
print("title: ",name.title())
print("swapcase: ",name.swapcase())

print("isupper: ",name.upper().isupper())
print("islower: ",name.lower().islower())
print("isalpha: ",name.isalpha())
print("istitle: ",name.title().istitle())
ascii_str=ascii("1")
print("isascii: ",ascii_str.isascii())




print('\n\n\n♥')
#defination of identifiers,isprintable and index's
perfect_identifier="name"
print("isidentifier: ",perfect_identifier.isidentifier())
check_str="kiran \n kumar"
print("isprintable: ",check_str.isprintable())#all whitespaces except te space are not printable
index_string="kiran is great kiran amoung of all kiran's in the kiran group"
print("index: ",index_string.index("kiran"))
print("rindex: ",index_string.rindex("kiran"))
print("index: ",index_string.index("kiran",13,40))
print("rindex: ",index_string.rindex("kiran",13,40))





print('\n\n\n2♥')
#using map and lambda for lists
n1=str(223)
n2='?2?3'
n3='??'
n4="five"
n5="  kiran is a good boy  "
n6=" "
n=[n1,n2,n3,n4,n5,n6]
print([i for i in n])
print("isdecimal: ",list(map(lambda x: x.isdecimal(),n)))
#we should use str calss method inside a map function
print("isdigit: ",list(map(str.isdigit,n)))

print("isnumeric: ",list(map(str.isnumeric,n)))
print("??".isnumeric())

print("isalpha: ",list(map(lambda x: x.isalpha(),n)))

print("isspace: ",list(map(str.isspace,n)))


print("inside upper: ",str.upper("this is upper"))
# to applay certain method if there are number of strings
# use map function
print(tuple(map(str.upper,["one","two",'three','four'])))
print(tuple(map(lambda s:s+"♥","kirankumar")))




print('\n\n\n3♥')
##translatee and maketrans functions
s1="12"
s2='21'
s3='diswith'
trg="opra 1 is replaced with opra 2 and opra 3  remove"
table=trg.maketrans(s1,s2,s3)
print('printing tabke trg.maketrans(s1,s2,s3) which is a dict of unicode cahar that are'
      'that are char to be replace and deleted\n',table)
x=[(chr(i),chr(i)) if j is None else (chr(i),chr(j)) for i,j in table.items() if j is not None]
print('the table values are converted unicode to chare: ',x)
print("""maketrans creates a table like 
ith ele of both str in two col where 
col 1 ele replaced with col2 ele """)
print("table=trg.maketrans(s1,s2,s3)",trg.translate(table))

print()
intab = "aeiou"
outtab = "12345"
deltab='!'
trantab = str.maketrans(intab, outtab,deltab)
print('maketrans table: ',trantab)
str = "this is string example....wow!!!"
print (str.translate(trantab))

import string
print(string.ascii_lowercase)
s4="####@#@#@#@#@#geeks for geeks       "
print(s4.strip('@#'))
s6="bad bad bad bad good person is kiran"
print(s6.replace("bad","very",3))


print("coutn fun")
print("no of \'bad\' string in the s6 from 3 to 11 are: ",s6.count("bad",0,3))



print("join fun")
strs=['a','b','c','d']
joined_str="#".join(strs)
print(joined_str)




print("string justification",end="\n")
s_just="kirankumar"
print()
print("center".center(40))
print(s_just.center(40,"♥"))
print()
print("ljust".center(40))
print(s_just.ljust(40,"♥"))
print()
print("rjust".center(40))
print(s_just.rjust(40,'♥'))
print()
print("".center(40,"♥"),"since len is 40 so the hearts are")

print()
print()

#startswith and endswith
dstring="kiran is great kiran"
print(dstring.center(60,"_"))
print("startswith kiran: ",dstring.startswith("kiran"))
print("endswith kiran: ",dstring.endswith("kiran"))

print("startswith kiran: ",dstring.startswith("kiran",0,5),end='/')
print("the stirng form 0 to 4 is: ",dstring[0:5])
print("endswith kiran: ",dstring.endswith("kiran",0,5),end='/')
print("the stirng form 0 to 4 is: ",dstring[0:5])
print()


print("startswith kiran: ",dstring.startswith("kiran",0,7),end='/')
print("the stirng form 0 to 7 is: ",dstring[0:7])
print("endswith kiran: ",dstring.endswith("kiran",0,7),end='/')
print("the stirng form 0 to 7 is: ",dstring[0:7])
print()


print("startswith kiran: ",dstring.startswith("kiran",15,20),end="/")
print("the stirng form 15 to 20 is: ",dstring[15:20])
print("endswith kiran: ",dstring.endswith("kiran",15,20),end="/")
print("the stirng form 15 to 20 is: ",dstring[15:20])
print()

print("startswith kiran: ",dstring.startswith("kiran",13,20),end="/")
print("the stirng form 13 to 20 is: ",dstring[13:20])
print("endswith kiran: ",dstring.endswith("kiran",13,20),end="/")
print("the stirng form 13 to 20 is: ",dstring[13:20])



