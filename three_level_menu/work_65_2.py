china = {
        "北京": {
            "一号线": ["四惠", "大望路", "天安门", "西单"],
            "二号线": ["北京站", "朝阳门", "东直门", "西直门"],
            "三号线": ["国贸", "三元桥", "知春路", "巴沟"]
            },
        "上海": {
            "四号线": ["徐家汇", "人民广场", "延长路", "共康路", "呼兰路"],
            "五号线": ["东昌路", "静安寺", "江苏路", "虹桥火车站"],
            "六号线": ["宝山路", "赤峰路", "曹阳路", "虹桥路", "宜山路"]
            },
        "广州": {
            "七号线": ["东山口", "农讲所", "烈士陵园", "公园前", "体育西路"],
            "八号线": ["黄边", "纪念堂", "三元里", "白云公园"],
            "九号线": ["沙河顶", "北京路", "一德路", "文化公园"]
            },
        "深圳": {
            "一号线": ["高新园", "桃园", "白石洲", "华侨城"],
            "四号线": ["白石龙", "明乐", "少年宫", "红山"],
            "五号线": ["大学城", "兴东", "西里", "深圳北站"]
            },
        }
city_lst=[]
subway_lst=[]
station_lst=[]
temp_dic={}
menu_len = 0
menu_level=1
temp_city=''
temp_subway=''
temp_station=''
def show_citys():
    global menu_len 
    for v,item in enumerate(china):
        city_lst.append(item)
        print(v,item)
    menu_len = len(china)

def show_subway(nu):
    global menu_len 
    global temp_dic
    temp_dic = china[city_lst[nu]]
    for v,item in enumerate(temp_dic):
        subway_lst.append(item)
        print(v,item)
    menu_len = len(subway_lst)

def show_station(nu):
    global menu_len 
    global temp_dic
    temp_dic = temp_dic[subway_lst[nu]]
    for v,item in enumerate(temp_dic):
        station_lst.append(item)
        print(v,item)
    menu_len = 0

def input_ansysis():
    global menu_level
    r = input(">>>")
    if r == 'q':
        exit()
    elif r == 'b' and menu_level > 1:
        menu_level -= 1
    elif r.isdigit():
        r = int(r)
        if r >= menu_len:
            print("列表中没有所示序号")
            return -1
        elif menu_level < 3:
            menu_level += 1
            return r;
    else:
        print("错误的输入")
        return -1

temp_number = 0
before_number = 0
while True:

    #城市列表
    if menu_level == 1:
        show_citys()
        city_number = input_ansysis()

    #地铁线列表
    elif menu_level == 2:
        show_subway(city_number)
        subway_number = input_ansysis()

    #地铁站列表
    elif menu_level == 3:
        show_station(subway_number)
        input_ansysis()
