Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
ans = "no"
ran = random.randint(10000,99999)
data = []


def login():
    first_name = input("enter your first name-:  ")
    first = first_name[:2]
    last_name = input("entet yourlast name-: ")
    last = last_name[:2]
    email = input("enter a valid email address-: ")
       
    password = first + last + str(ran)
    print("/n This is your automated PASSWORD", password )
    ans = input("/n are you okay with this password? -: ")

    if ans == "yes":
        print("/n /n firstname  ",first_name)
        print("/n lastname. ", last_name)
        print("/n email address  ", email)
        print("/n password. " ,password)
    else:
     password = input(" enter the password of you choice. -: ")

     while len(password)< 7:
         print("/n password must be seven characters")
         password = input("re-enter password.-: ")
     else:
         print("/n /n firstname. ", first_name)
         print("/n lastname. ", last_name)
         print("/n email address. ", email)
         print("/n password. " ,password)
     data.append([ first_name, last_name, email, password])

login()
print (data)


 
Reply
Forward
