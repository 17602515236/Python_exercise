import json

data = {
        'name':[
            {'id':1,"age":24},
            {'id':2,"age":22}
            ]
        }
d1 = json.dumps(data)
#序列化data，此时d1(str)可以直接通过write写入文件
print(d1,type(d1))
d2 = json.loads(d1)
#反序列化d2，转化为原来的格式
print(d2,type(d2))
#output:
#{"name": [{"id": 1, "age": 24}, {"id": 2, "age": 22}]} <class 'str'>
#{'name': [{'id': 1, 'age': 24}, {'id': 2, 'age': 22}]} <class 'dict'>


#将data结构序列化后写入file
f = open("./test.txt",'w')
json.dump(data,f)
f.close()
#读取./test.txt文件的内容(内容是str)后
f = open("./test.txt",'r')
data = json.load(f)
print(data,type(data))
f.close()
#output:
#{'name': [{'id': 1, 'age': 24}, {'id': 2, 'age': 22}]} <class 'dict'>
