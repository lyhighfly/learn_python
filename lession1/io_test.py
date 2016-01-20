#!/usr/bin/env python
#coding=utf-8

#python中的file操作是对底层c文件操作的一种封装，使其使用更简单一些；

#文件不存在会报IOError，后面跟随打开文件的方式
try:

	file = open("/Users/liuyu/git_test/learn_python/lession1/file",'r')
except:
	print 'file open failed'
finally:
	if file:
		file.close()
#同一时间系统可打开的文件有限，不使用的file要close

#file关闭再尝试从文件进行读取就会ValueError：I/O operation on closed file
#file.read()

#简洁的写法，不用自己手写关闭file
with open("/Users/liuyu/git_test/learn_python/lession1/file",'r') as f:
	print f.read()#这样会将文件内容全部读取

file = open('./file','r')
print file.read(5)
#同一个文件的读取会是叠加态效果！！！
for line in file.readlines():
	print line.strip()

#file-like object:可进行read操作的对象，不必从特定类继承，只要实现read()方法
#codecs提供模板进行转换编码，暂时跳过
imagefile = open('./992.jpg','rb')
imagefile.read()

#r 读 rb 读二进制  w 写   wb  写二进制  w+ 追加模式
with open('./file','w+') as f:
	f.write('\nhello world')


