#teranary operator
n = 9
print("Hello") if n==9 else print("Goodbye")


m='hello' if n<9 else 'goodbey'
print(m)

n=n+1 if n==9 else n+5
print(n)



#nested teranary operator
n = 9
print("Hello") if n==9 else print("Goodbye") if n==5 else print('good day')


m='hello' if n<9 else 'goodbey' if n==5 else 'good day'
print(m)

#we cannot use any assignment/inplace_operator in conditional expression
# n = 9
# try:
#     n+=1 if n == 9 else n+=5 if n == 5 else n=10
#     print(n)
# except:
#     print("raised SyntaxError: invalid syntax")
#since its showing the error no useof  try and except blocks still the code termenates incorrectly


# but we can use the arithemetic operations and assign the result to a var
n = 9
n=n+1 if n==9 else n+5 if n==5 else 10
print(n)
