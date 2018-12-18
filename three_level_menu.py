china_ditie = {
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

#获得输入并检查
def verify_input(__list):
    while True:
        if __list is city_lst:
            help_str = "请输入需要查询的城市(q退出):"
        elif __list is subway_lst:
            help_str = "请输入需要查询的铁路线(b返回上级，q退出):"
        else:
            help_str = "(b返回上级，q退出):"

        #打印帮助并获取输入
        _input = input(help_str)
        if _input == 'q':
            exit()
        elif _input == 'b':
            return _input
        elif _input.isdigit():
            _input = int(_input)
            if _input > len(__list):
                print("超出限制")
                continue
            return _input
        else:
            print("错误指令")

#显示城市菜单
city_lst=[]
def show_city():
    print("===================================")
    for lv,city in enumerate(china_ditie.keys(),1):
        print(lv,city)
        city_lst.append(city)#将city添加到列表
    print("===================================")
    return verify_input(city_lst)

#显示地铁线菜单
subway_lst=[]
city_dict={}
def show_subway_line(city_num):
    global city_dict
    print("===================================")
    city_dict = china_ditie[city_lst[city_num - 1]]
    for lv,subline in enumerate(city_dict,1):
        print(lv,subline)
        subway_lst.append(subline)
    print("===================================")
    return verify_input(subway_lst)
    
#显示地铁站信息
station_lst=[]
def show_subway_station(subway_num):
    print("===================================")
    subway_dict = city_dict[subway_lst[subway_num - 1]]
    for lv,station in enumerate(subway_dict,1):
        print(lv,station)
        station_lst.append(station)
    print("===================================")
    return verify_input(station_lst)

#start
while True:#城市
    city_num = show_city()
    if city_num == 'b':
        print("顶层目录")
        continue
    while True:#地铁线
        subway_num = show_subway_line(city_num)
        if subway_num == 'b':
            break
        while True:
            ret = show_subway_station(subway_num)
            if ret != 'b':
                print("底层目录")
            else:
                break

