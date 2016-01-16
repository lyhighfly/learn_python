#!/usr/bin/env python 
#coding=utf-8

#use list
#list中，元素可以是任意类型，可以混合使用，可以通过索引遍历，可以改变其中的值
list =['a',"b",100,True]
for member in list:
	print 'list member:%s' %member
list[2] = 200
print 'After Change list:\n'
for member in list:
	print 'list member:%s' %member

#use tuple
#tuple 元组类型数据，可以任意类型元素，但是初始化之后就不能改变其值了
tuple = ('a',"b",100,True)
for member in tuple:
	print 'tuple member:%s' %member
#这样是不会成功的，因为元组中的元素是不能改变的
print 'Try to Change Tuple member'
#tuple[2]="c"

#but 当tuple包含list的时候，元素却可以改变了，类似于tuple的const指针，不能通过这个指针来修改其中的元素
tuple = ('a',"b",100,True,list)
tuple[4][2] = 300


#use dict
#字典就是可以放置任意的key-value对
dict = {'a':100,"b":200,300:400,True:False}
for (key,value) in dict.items():
	print 'dict %s member value is : %s' %(key,value)
#也可以使用不带括号的方式去遍历元素，感觉有点类似php中的map遍历
#这两种可能会有性能上的差异，先不深究了:P
for key, value in dict.items():
	print 'dict %s member value is : %s' %(key,value)

#加入dict中包含了重复的key，会有什么效果：
dict = {'a':100,"a":200}
for key, value in dict.items():
	print 'dict %s member value is : %s' %(key,value)
#结果证明，是根据key的哈希值来放置value的，相同的key的情况下，后算哈希的key的value会将前算的value顶替掉
#dict 的key值必须是不可变的元素，不能使用list作为dict的key！！！

#use set
#set 貌似通用编程语言中的set都是放置不重复元素的集合类的统称，这获取就是一通百通的意思吧，大差不差
array1 = [1,2,2,2,2,2,3,4,5,6]
array2 = [3,4,5,6,7,8]
set1 = set(array1)
set2 = set(array2)

for item in set1:
	print "set1 member is:%d" %item

set1.add(7)
for item in set1:
	print "set1 member is:%d" %item
set1.remove(2)
#不能删除没有的key，会报错：KeyError
#set1.remove(8)
for item in set1:
	print "set1 member is:%d" %item 
#set 与 set 之间，可以进行集合的运算
set1 & set2
set1 | set2
set1 ^ set2
