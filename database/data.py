# import sqlite3
# connection = sqlite3.connect('database/sms.sqlite3')

# cursor = connection.cursor()

# cursor.execute ("""                
#  CREATE TABLE IF NOT EXISTS students(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                name VARCHAR(100),
#                phone VARCHAR(100),
#                address VARCHAR(100)

#                 )
# """)
# # to add data


# connection.commit()

# cursor.execute("""
#    INSERT INTO students(name, phone, address) 
#             VALUES('JOHN DOE', '12345', 'ABC STREET')

# """)

# connection.commit()

#**********

## to ask data to user

# def add_student(name, phone, address):
#     cursor.execute("""
#     INSERT INTO STUDENTS( name, phone, address) VALUES(?,?,?)
#     """, (name, phone, address))
#     connection.commit()

# name=input("enter name :")
# phone= input("enter phone :")
# address= input("enter address")
# add_student(name, phone, address)


# # to see data

# def show():
#     cursor.execute("""
#       SELECT * FROM students
#      """)
#     print(cursor.fetchone())
#     print(cursor.fetchmany())
#     print(cursor.fetchall())
    
# show()

# # to delete data

# def delete(id):
#     cursor.execute("""
#     DELETE FROM students WHERE id = ?                           
#     """, (id))
#     connection.commit ()

# delete(1)
    

## to update data

# def update(id,name,phone,address): 
#     cursor.execute(''' 
#     UPDATE students SET name = ?, phone = ?, address = ? WHERE id = ? 
                    
#     ''',(name,phone,address,id)) 
#     connection.commit() 
# update(3,'hari','12345','Nairobi')


