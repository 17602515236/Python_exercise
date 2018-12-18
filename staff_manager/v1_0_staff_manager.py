#解析输入命令
#解析成功则返回字典类型，否则返回None并打印input error
#字典类型filed(list)，table(str),condition(str)
def ansysis_command(command_str):
    ret_dic = {}
    cmd = command_str.split()

    if 'find' in cmd and 'from' in cmd and 'where' in cmd:
        n_fi = cmd.index('find')
        n_fr = cmd.index('from')
        n_wh = cmd.index('where')

        ret_dic['filed'] = cmd[n_fi + 1 : n_fr]
        ret_dic['table'] = ' '.join(cmd[n_fr + 1 : n_wh])
        ret_dic['condition'] = ' '.join(cmd[n_wh + 1 :])
        return ret_dic
    else:
        print("input error")



#获取文件的排列格式
def get_file_format(file_name):
    format_dic={}
    f = open(file_name,mode= 'r')
    file_format = f.readline().strip().split(',')
    for v,item in enumerate(file_format):
        format_dic[item] = v
    f.close()
    return format_dic

file_format = get_file_format("./staff.txt")
print(file_format)
ansys_dic = ansysis_command("find name age from staff_table where age > 20")
if ansys_dic != None:
    #打开文件
    #按行读取
    #首先判断条件
    #如果满足条件：打印对应字段
    #如果不满足：跳过
    f = open("./staff.txt",mode= 'r')
    f.readline()
    for line in f:
        line = (line.strip()).split(',')
        print(line)
    f.close()

