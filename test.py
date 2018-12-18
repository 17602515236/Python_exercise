"""
name2 = ['old_driver', 'rain_jack', ['old_boy', 'old_girl'], 'shanshan', 'peiqi', 'alex', 'black_girl', 1, 2, 3, 4, 2, 5, 6, 2]

print(name2)
index_2 = name2.index(2)
print(index_2)
index_22 = name2.index(2,index_2 + 1)
print(index_22)
for i in name2:
    n = name2.index(i)
    if n%2 == 0:
        name2[n]=-1
    print(n,name2[n])
"""

products = [['iphne8',6888],['MacPro',14800],['xiaomi8',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
products_car=[]
def show_product():
    for i,v in enumerate(products):
        print(i,'.',v[0],'\t',v[1])

def get_user_product():
    u_in = input("Please input the product you want with number>>>")
    if u_in.isdigit():
        u_in = int(u_in)
        if u_in >= len(products):
            print("No products")
        else:
            products_car.append(products[u_in])
    if u_in == 'q':
        for i in products_car:
            print(i)
        exit()
    else:
        print("Error command!")
#start:
while True:
    show_product()
    get_user_product()
