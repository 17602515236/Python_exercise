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
            t += 1
            print("input error times of",t)
            f.close()
    else:
        print("input error three times,exit")
        f.close()
        return -1
def welcome(info_lst):
    print("---------------------weclome:{}---------------------".format(info_lst[2]))


def get_cmd(input_lst):
    cmd = input(">>>")
    if cmd == 'q':
        exit()
    if cmd.isdigit():
        cmd = int(cmd)
        if cmd >= len(input_lst):
            print("未知命令")
        else:
            return cmd
    else:
        print("error command")
    return -1

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


inter_lst=[['打印信息',show_info],['修改信息',motify_info],['修改密码']]
def show_help():
    for v,i in enumerate(inter_lst):
        print("{}\t{}".format(v,i[0]))


    
lst = login()
welcome(lst)
while True:
    show_help()
    cmd = get_cmd(inter_lst)
    if cmd != -1:
        inter_lst[cmd][1](lst)
