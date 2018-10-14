
from django.shortcuts import render_to_response
import getpass
import datetime


global dic
dic = {"fentiao": "redhat", "wang": "redhat"}
time = []
global loginsig
loginsig = 0
global loginuser
def login():
        a = 0
        b = 0
        global loginsig
        global loginuser
        name = input("Please input username:")
        lastlogintime = datetime.datetime(2017, 3, 30, 21, 2, 4)
        password = ""
        while (a < 2):
            if name.lower() in dic == False:
                name = input("user error,input again:")
                a = a + 1
            else:
                break
        if a == 2 and name.lower() in dic == False:
            print("login failed!")
        else:
            password = getpass.getpass("Please input password:")
            while (b < 2):
                if password != dic.get(name.lower()):
                    password = getpass.getpass("password error,    input again:")
                    b = b + 1
                else:
                    break
            if b == 2 and password != dic.get(name.lower()):
                print("login failed!")
            else:
                print("login successful")
                loginsig = 1
                loginuser = name.lower()
                t1 = datetime.datetime.now()
                time.append(t1)
                print(t1)
                if len(time) == 1:
                    print("this is login first")
                else:
                    if (t1 - time[len(time) - 2]).seconds < 14400:
                        print("you already logged at %s") % time[len(time) - 2]
                print(loginsig)
                showmenu()

def showuser():
        if loginsig == 0:
            print("please login first!")
        if loginsig == 1:
            for i in range(0, len(dic.keys())):
                print(dic.keys()[i], "\n")
        showmenu()

def remove():
        if loginsig == 0:
            print("please login first!")
        if loginsig == 1:
            if loginuser == "fentiao":
                for i in range(0, len(dic.keys())):
                    print(dic.keys()[i], "\n")
                delname = input("you want to delete:")
                dic.pop(delname)
                print(delname, "deleted")
            else:
                print("you have no permission to rmove user!")
        showmenu()

def showmenu():
        print("""
                a.login
                b.remove
                c.showuser
                d.quit""")
        num = input("your choice:")
        if num == 'a':
            login()
        elif num == 'b':
            remove()
        elif num == 'c':
            showuser()
        else:
            return


