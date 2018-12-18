dic = {'k1':'v1','k2':'v2','k3':'v3'}

'''
#便利所有keys
for i in dic.keys():
    print(i)
#便利所有values
for i in dic.values():
    print(i)
#遍历所有的key和value
for i in dic.keys():
    print(i,dic[i])
#添加键值对
dic['k4']='v4'
print(dic)
#删除键值对
del dic['k1']
print(dic)
#删除键值对，如果不存在不报错并返回None
ret = dic.get('k5')
print(ret)
if ret != None:
    print("delete")
    dic.pop('k5')
#更新
d1 = {'k1':'v111','a':'b'}
d2 = {'k1':'v1','k2':'v2','k3':'v3','a':'b'}
d1.update(d2)
print(d1)
#改值
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
lis[0][1][2]['k1'][0] = 'TT'
lis[0][1][2]['k1'][1] = '100'
lis[0][1][2]['k1'][2] = 101
print(lis)
'''
#模拟
li=[1,2,3,'a','b','4','c']
d = {'k1':[]}
if d.get('k1') == None:
    d.setdefault('k1')
if isinstance(d['k1'],list) == True:
    d['k1'] = li[0::2]

print(d)
