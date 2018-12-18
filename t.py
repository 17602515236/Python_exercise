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
def show_city():
    city_lst.clear()
    for v,item in enumerate(china):
        city_lst.append(item)
        print(v,item)

def show_subway(number):
    subway_lst.clear()
    for v,item in enumerate(china[city_lst[number]]):
        subway_lst.append(item)
        print(v,item)
        
def show_station(city,subway):
    station_lst.clear()
    for v,item in enumerate(china[city_lst[city]][subway_lst[subway]]):
        station_lst.append(item)
        print(v,item)

def check_input(lst):
    r = input(">>>")
    if r == 'q':
        exit()
    elif r == 'b':
        return r
    elif r.isdigit():
        r = int(r)
        if r >= len(lst):
            print("overload")
            return -1
        else:
            return r
    else:
        print("Error CMD")
        return -1
level = 1
while True:
    if level == 1:
        show_city()
        ret = check_input(city_lst)
        if ret == 'b':
            print("已经到顶")
        elif ret >= 0:
            level += 1
    if level == 2:
        show_subway(ret)
        ret2 = check_input(subway_lst)
        if ret2 == 'b':
            level -= 1
        elif ret2 >= 0:
            level += 1
    if level == 3:
        show_station(ret,ret2)
        ret3 = check_input(station_lst)
        if ret3 == 'b':
            level -= 1
        elif ret >= 0:
            print("已经到了底层目录")
#方法2
'''
while True:
    show_city()
    ret = check_input(city_lst)
    if ret == 'b':
        print("已经到顶")
    elif ret >= 0:
        while True:
            show_subway(ret)
            ret2 = check_input(subway_lst)
            if ret2 == 'b':
                break
            elif ret2 >= 0:
                while True:
                    show_station(ret,ret2)
                    ret3 = check_input(station_lst)
                    if ret3 == 'b':
                        break
                    elif ret >= 0:
                        print("已经到了底层目录")
                        '''
