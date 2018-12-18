products = [['iphne8',6888],['MacPro',14800],['xiaomi8',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]

shopping_cart=[]
salary=0
shopping_count=0
#获取薪资
def get_salary():
    while(True):
        temp = input("Please input your salary>>>")
        if temp.isdigit():
            return int(temp)
        elif temp == 'q':
            exit()
        else:
            print("input error,please try again")
     
def show_products():
    for v,item in enumerate(products):
        print("%d\t%s\t%s"%(v,item[0],item[1]))
    
def add_shopping_cart(no,sp_ct):
    global shopping_count
    product_price = int(products[no][1])
    if salary < (shopping_count + product_price):
        print("余额不足")
    else:
        sp_ct.append(products[no])
        shopping_count += product_price

def show_shopping_cart(sp_ct):
    global shopping_count
    print("---------shopping cart----------")
    for v,item in enumerate(sp_ct):
        print("%s\t%s"%(v,item))
    print("All count = {}".format(shopping_count))
    print("Left ={}".format(salary - shopping_count))
    print("--------------------------------")

def input_ansysis():
    recv = input("请输入想要购买的商品>>>")
    if recv == 'q':
        exit()
    elif recv.isdigit():
        p_no = int(recv)
        if p_no >= len(products):
            print("没有这样的商品")
            return -1
        else:
            return p_no
    else:
        print("错误的命令")
        return -1
        print
            


salary = get_salary()
while True:
    show_products()
    num = input_ansysis()
    if num >=0:
        add_shopping_cart(num,shopping_cart)
    show_shopping_cart(shopping_cart)

    

