# data=[
# ['ram','shyam','hari'],
# ['gita','sita','rita']
# ]
# name=input("enter name")
# if name in data [0]:
#     print( f"hello : {name}")
# elif name in data[1]:
#     print(f"hello : {name}")
# else:
#     print('no name found')

# user={
#     'username': "admin",
#     'password': "admin"
# }
# username=input("enter username")
# password=input("enter password")
# if user['username']== username and user['password']== password :
#     print('valid')
# else:
#     print('invalid')


# x=6
# y=5
# z=56
# a=6
# if x>y and x>z and z>a :
#     print(' x is greater')
# elif y>x and y>z and y>a:
#     print('y is greater')
# elif z>x and y<z and z>a:
#     print('z is greater')
# else:
#     print('a is greater')



# x=input('enter number')

# y=input('enter number')

# z=input('enter number')

# if x>y and x>z and y>z:
#     print(x)
#     print(y)
#     print(z)
# elif x>y and x>z and z>y :
#     print(x)
#     print(z)
#     print(y)
# elif y>x and y>z and x>z :
#     print(y)
#     print(x)
#     print(z)
# elif y>x and y>z and z>y :
#     print(y)
#     print(z)
#     print(x)
# elif z>x and z>y and x>y :
#     print(z)
#     print(x)
#     print(y)
# else:
#     print(z)
#     print(y)
#     print(x)


x= input('enter 1st number :')
y= input('enter 2nd number :')
option= input(''' 
              1.add
              2.sub
              3.mul
              4. div''')
print("choose one option")
if option== '1' :
    z=x+y
    print(z)
elif option=='2':
    z=x-y
    print(z)
else:
    z=x*y
    print (z)