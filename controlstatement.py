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



# wronggggggg

# amount='20000'
# pin="1234"
# pin1 = input("enter your pin :")
# if pin1==pin :
#  print("welcome to the system")
#  print("what do you want")
#  option= input ('''
#           1. check balance
#           2. widthdraw amount''')
#  if option == "1":
#   print("your current balance is :",amount)
#  elif option== "2":
#     x = input("enter the amount")
#     if x< amount:
#        print('withdrawn successful')
#     elif x==amount:
#        print('cannot withdraw all amount')
#     else:
#        print (' insufficient')
#     #  z = amount-x
#     #  print(f"Remaining balance: {z}") 
  
#  else:
#   print("input invalid")
# else:
#  print("incorrect pin entered")





                                 #   loop
# x=1
# while x<=10 :
#     print(x)
#     x+=1


# data= [11,22,33,44]
# a=0
# while  a< len(data):
#     print (data [a])
#     a+=1

# x=0
# while x<=20:
#     print(x)
#     x+=2
# y=1
# while y<=20: 
#     print(y)
#     y+=2


# data=[
#     [10,20,30,40,50],
#     [50,100,150,200,250]
# ]
# a=0
# ft=0
# lt=0
# # a= print(data[0]+data[1])
# while  a<len (data):
#    ft+=data[a][0] 
#    lt+=data[a][-1]
#    a+=1
# print(ft)
# print(lt)
   


a=1
b=1
while a<=10:
 print(f"1 * {b}={a}")
 a+=1
 b+=1


x=int(input("enter a number"))
y=1
while y<=10:
 z= x*y
 print(f"{x}*{y}={z}")
 y+=1

 