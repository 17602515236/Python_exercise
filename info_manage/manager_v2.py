import os
def login():
    t = 0
    while t < 3:
        users = input("user:")
        passwd = input("password:")
        f = open('./info.txt',mode = 'r')
        for v,i in enumerate(f):
            i = i.strip().split(',')
            if users == i[0] and passwd == i[1]:
                f.close()
                return i
        else:
            f.close()
            t += 1
            print("input error times of",t)
    else:
        print("input error three times,exit")

def welcome(info_lst):
    print("---------------------weclome:{}---------------------".format(info_lst[2]))

"""
def show_info(info):
    print("--------------------------用户信息-------------------------")
    print("{:12}{:12}{:12}{:12}{:12}".format('users','password','name','age','position'))
    print("{:12}{:12}{:12}{:12}{:12}".format(info[0],info[1],info[2],info[3],info[4]))
    print("-----------------------------------------------------------")
def motify_info(info):
    #打印需要修改的属性
    print("0.{:12}\n1.{:12}\n2.{:12}\n3.{:12}\n4.{:12}".format('修改用户名','修改密码','修改姓名','修改年龄','修改职位'))
    no = get_cmd(info)
    if no != -1:
        new_v = input("please input new value:")
        if new_v == '':
            print("Empty input")
            return
        print(','.join(info))
        f = open('./info.txt',mode = 'r+')
        f_n = open('./info.new',mode = 'w')
        for line in f:
            if ','.join(info) in line:
                info[no] = new_v
                f_n.write(','.join(info) + '\n')
            else:
                f_n.write(line)
        f.close()
        f_n.close()
        os.rename('./info.new','./info.txt')
"""

def show_and_get_cmd(cmd_lst):
    #show cmd
    for v,item in enumerate(cmd_lst):
        print(v,item)
    #get serial
    ret = input(">>>")
    if ret == 'q':
        exit()
    elif ret.isdigit():
        ret = int(ret)
        if ret >= len(cmd_lst) or ret < 0:
            print("overload!")
        else:
            return cmd_lst[ret]
    else:
        print("error command!")


def motify_passwd(current_usr):
    old_psw = input("输入原密码:")
    if old_psw == current_usr[1]:
        new_psw1 = input("输入新密码:")
        new_psw2 = input("再次输入新密码:")
        if new_psw1 == new_psw2:
            f = open('./info.txt',mode = 'r+')
            f_n = open('./info.new',mode = 'w')
            for line in f:
                if ','.join(current_usr) in line:
                    current_usr[1] = new_psw1
                    f_n.write(','.join(current_usr) + '\n')
                else:
                    f_n.write(line)
            f.close()
            f_n.close()
        else:
            print("两次输入的密码不相同")
    else:
        print("原密码错误")




def motify_info(current_usr):
    ret = show_and_get_cmd(['修改用户名','修改姓名','修改年龄','修改职位'])
    if ret != None:
        val = input("输入新值:")
    #写入文件
        f = open('./info.txt',mode = 'r+')
        f_n = open('./info.new',mode = 'w')
        for line in f:
            if ','.join(current_usr) in line:
                if ret == '修改用户名':
                    current_usr[0] = val
                elif ret == '修改姓名':
                    current_usr[2] = val
                elif ret == '修改年龄':
                    if val.isdigit() and int(val) >= 0:
                        current_usr[3] = val
                    else:
                        print("错误的年龄")
                elif ret == '修改职位':
                    current_usr[4] = val
                f_n.write(','.join(current_usr) + '\n')
            else:
                f_n.write(line)
        f.close()
        f_n.close()
        os.rename('./info.new','./info.txt')


def show_info(current_usr):
    print("-------------用户信息---------------")
    print("{}:\t{}".format("用户名",current_usr[0]))
    print("{}:\t{}".format("密码",current_usr[1]))
    print("{}:\t{}".format("姓名",current_usr[2]))
    print("{}:\t{}".format("年龄",current_usr[3]))
    print("{}:\t{}".format("职位",current_usr[4]))
    print("--------------------------------")
    
lst = login()
if lst == None:
    exit()
welcome(lst)
while True:
    cmd = show_and_get_cmd(['打印信息','修改信息','修改密码'])
    if cmd == '打印信息':
        show_info(lst)
    elif cmd == '修改信息':
        motify_info(lst)
    elif cmd == '修改密码':
        motify_passwd(lst)
