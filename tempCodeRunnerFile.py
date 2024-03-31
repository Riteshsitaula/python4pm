data =[
    {'name':"ram", 'gender':"male"},
    {'name':"sita", 'gender':"female"},
    {'name':"hari", 'gender':"male"},
]
def male():
    for user in users:
        if user ['gender']=='male':
        print(user)


def female():
    for user in users:
        if user ['gender']=='female':
        print(user)
male()
female()
