import getpass
i=0
while i<3:
    user_name = input("input your user name:")
    passwd = getpass.getpass("input your password:")
    if(user_name == "zhj" and passwd == "a"):
        print("hello"+user_name)
        break
    else:
        print("error user_name")
    i+=1
else:
    print("locked")


