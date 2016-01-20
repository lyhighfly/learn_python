#!/usr/bin/env python
#coding=utf-8

import json
#序列化pickling 反序列化unpickling  
try:
	import cPickle as pickle
except ImportError:
	import pickle

#pickling unpickling示范
with open('./pickfile','w') as file:
	b = {100:'l',200:'y','300':True}
	pickle.dump(b,file)

try:
	readfile = open('./pickfile','r')
	b = pickle.load(readfile)
	for key,value in b.items():
		print 'key',key,'value',value
except StandardError:
	print 'read file error'
finally:
	if readfile:
		readfile.close()

#序列化是专用的，不能语言之间的pickling unpickling 混用

#json和python数据之间的转换，注意json转换python之后的数据显示
d = {1:2,'2':'3',"3":True}
jsonobj = json.dumps(d)
print jsonobj

dd = json.loads(jsonobj)
print dd

class Student:

	def __init__(self,name,age):
		self.name = name
		self.age = age
	
student = Student('liuyu',10)
#直接类实例转json是不成功的，TypeError
#stujson = json.dumps(student)

#需要写对应转换方法，类似java中需要传输的类需要实现序列化函数
#并在json的dumps 使用default参数
def student2dict(std):
	return{
			'name':std.name,
			'age':std.age
			}

studjson = json.dumps(student, default=student2dict)
print studjson
