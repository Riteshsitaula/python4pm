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


# x= int (input ('enter 1st number :'))
# y= int (input('enter 2nd number :'))
# print("choose one option :") 
# option = input (''' 
#               1. add
#               2. sub
#               3. mul
#               4. div ''')

# if option=="1":
#     print(" result :",x + y)
# elif option=='2':
#     print(" result :",x-y)
# elif option=='3':
#     print(" result :",x*y)
# else:
#     print (" result :",x/y)


amount='20000'
pin="1234"
pin1 = input("enter your pin :")
if pin1==pin :
 print("welcome to the system")
 print("what do you want")
 option= input ('''
          1. check balance
          2. widthdraw amount''')
 if option == "1":
  print("your current balance is :",amount)
 elif option== "2":
    x=input("enter the amount")
    if x< amount:
     print('insufficient')
    elif x==amount:
     print('cannot withdraw all amount')
    else:
     print (' withdrawn successful')
    #  z = amount-x
    #  print(f"Remaining balance: {z}") 
  
 else:
  print("input invalid")

  

else:
 print("incorrect pin entered")
