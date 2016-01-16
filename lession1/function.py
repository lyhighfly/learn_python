#!/usr/bin/env python
#coding=utf-8

#function define
def my_abs(x):
#使用了类型判断 isinstance  类似于java中的 .instanceof()
#isinstance()第一个参数为测试数据，第二个可以是单个的classinfo,也可以是一个classinfo的tuple：(int,float,str,set,tuple,list)
#raise 抛出异常，类似java中的throw Exception
	if not isinstance(x, (int, float)):
		raise TypeError("x is not right type")

	if x >= 0:
		return x
	else:
		return -x
#return 可以是任意类型数值，return 意思是返回return None
#可以使用pass代替任何执行语句，感觉类似于java中的abstract method，暂时没有想好怎么写，但是使用pass可以让系统顺利编译通过
def my_nothing():
	pass

def my_type(x):
	if not isinstance(x, set):
		raise TypeError("x is not a set")
def my_type1(x):
	if not isinstance(x, list):           #function 参数的个数，类型不对的时候，都会报：TypeError
		raise TypeError("x is not a list")
a = -10
b = my_abs(a)
print 'b abs is',b

b = my_abs(-10)

s = set([1,2,3])
my_type(s)
#my_type1(s)
s1 = [1,2,3,4]
my_type1(s1)

#返回多个值的情况,这种情况，接收顺序应该和函数返回顺序一样，其实move返回的是一个tuple
def move(x,y):
	x = x*1.1
	y = y*2.2
	return x,y

x = 100
y = 100

x1, y1 = move(x,y)
print 'move (%d,%d) to (%d,%d)' %(x,y,x1,y1)

#和c一样，可以在function定义是，指定默认参数，必须是不可变对象，这个默认项必须在function定义的最后面，作用和c一·，类似于java中的函数重载
def move(x, y=200):
	pass

#将集合元素 分别传参
def listparams(*array):
	pass

#可以定义关键字参数
def keyparams(name, age, **kw):
	print "name",name," age",age," others",kw

#此时，就可以只传必选参数
keyparams('liuyu',28)
#也可以选择任何数量的关键字参数
#注意此时info传递的方式方法,而且必须是dict类型的数据
info = {"company":"sogou","city":"Beijing"}
keyparams("liuyu",28, **info)

#必选参数，默认参数，可变参数，关键字参数可以集合使用
def allparams(a, b , c=3, *arg, **kw):
	print 'a',a,'b',b,'c',c,'arg',arg,'kw',kw,'\n'

#关键就是  arg必须是tuple，kw必须是dict
arg = ('w','o','w')
kw = {"just":"say"}
allparams(1,2,3,*arg,**kw)
allparams(1,2,*arg,**kw)
allparams(1,*arg,**kw)
allparams(*arg,**kw)
arg = ("w","o")
#这样就会因为参数不够，而报错了，只要可选参数的个数起码等于必选参数，才会成功，此时默认参数就会因为可选参数不够而自动取默认值
allparams(*arg,**kw)
