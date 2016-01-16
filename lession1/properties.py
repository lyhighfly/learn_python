#!/usr/bin/env python
#coding=utf-8

#properties1:slice 意指将list、tuple中的指定区域元素取出

array = []
n = 100
while n>0:
	array.append(n)
	n = n-1
print 'array member:',array

array1 = array[0:30]
print 'array1 member:',array1
#slice 可以是负索引，和list索引一样
#由于tuple也是一种特殊的list，所以也只是slice动作
#可以使用步进选择slice元素
array2 = array[10:50:2]
print 'array2 member:',array2

#字符串也可以slice，只是元素是字符
string = 'abcdef'
string1 = string[0:5:2]
print 'string member:',string1


#properties2:iteration  只要是迭代对象，不管有无小标，都可以迭代遍历元素（多废话）

#默认遍历的是key值
d = {1:"a",2:"b",3:"c"}
for key in d:
	print 'key is ',key

#迭代key value的方法
for key,value in d.iteritems():
	print key, value

#字符串也是可以迭代遍历的
#可以通过isinstance(x, Iterable)来判断x是否是可以迭代的对象

#list可以通过enumerate转换成数字索引-value对
for key, value in enumerate(array2):
	print '%d value is %s' %(key, value)


#properties3:List Comprehensions   列表生成器

array = range(1,100,5)
print array

index = 0
#如果需要将生成的list的每个元素进行相同的变化呢？
for value in array:
	array[index] = value*value
	index = index+1
print array
#loop生成list的方式太繁琐了

#可以使用List Comprehensions
#使用方法，以下：
array1 = [x*x for x in range(1,10)]
print array1
array2 = [x*x for x in range(1,10) if x%2==0]
print array2
array3 = [x*y for x in range(1,10) for y in range(10,20)]
print array3
array4 = [x*y for x in range(1,5)if x%2==0 for y in range(5,10)if y%2==0]
print array4

set1 = set([x*x for x in range(1,10)])
print set1


#properties4: generator  List Comprehensions需要一次性创建所有元素，占用空间和时间，使用generator 只在需要的时候去计算元素
#定义方式和List Comprehensions非常相似
generator = (x*x for x in range(1,10))
for g in generator:
	print g
#手动调用方式为g.next(),没有更多元素是  就会报：StopIteration的错误

def fabbi(max):
	n, a, b = 0,0,1
	while(n<max):
#将print 换成 yield  就将fabbi函数变成了generator，每次next都执行到yield出，下次继续yield之后的开始执行
		#print b
		yield b
		a,b = b, a+b
		n = n+1

#print fabbi(10)
for value in fabbi(10):
	print value



#更好的立杰generator的函数：
def stepshow():
	print 'step1'
	yield 1
	print 'step2'
	yield 2
	print 'step3'
	yield 3
step = stepshow()
step.next()#show step1
step.next()#show step2
step.next()#show step3
step.next()#stopIteration
#注意，next()是继续往下执行，而不是从头执行到yield处停止
