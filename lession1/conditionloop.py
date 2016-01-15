#!/usr/bin/env python
#coding=utf-8

age = 20
#raw_input读入的永远是字符串，需要进行转型，正好也学到了转型方法，和c java括起来的对象正好相反
age = int(raw_input('please input your age'))
if age > 20:
	print 'too old'
elif age == 20:
	print 'ok'
else:
	print 'too young'

#if的判断也可以简写 
#if x:
#    print ...
#只要x为非零数值,非None，非空字符串，非空list等  就返回True
#x = None
x = 0
if x:
	print "x is valid value"
else:
	print "x is invalid value"

#循环
#可以使用range(n)用于生成0-N的整数数组，当然这个也和c，中的api差不多，可以定义起始，步进
num = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in num:
	sum += i
print 'sum :%d'%sum


#我嘞个擦擦，python居然没有自增自减运算符：++ --
m = 10
sum = 100
while m > 0:
	print 'sum :%d' %(sum)
	m -=1

