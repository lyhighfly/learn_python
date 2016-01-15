#!/usr/bin/env python
#coding=utf-8

alphabet = ['a','b','c','d']

print 'alphabet[0]:',alphabet[0]
print 'alphabet[1]:',alphabet[1]
print 'alphabet[2]:',alphabet[2]
print 'alphabet[3]:',alphabet[3]
print 'alphabet[-1]:',alphabet[-1]
print 'alphabet[-2]:',alphabet[-2]
#可以进行负索引的查询，但是负索引的查询只能索引一个轮回，超过一个轮回，就会报：IndexError：list index out fo range
#print 'alphabet[-5]:',alphabet[-5]

#
alphabet.append('e')
print 'alphabet[4]:',alphabet[4]
alphabet.insert(5,'f')
print 'alphabet[5]:',alphabet[5]
print 'length alphabet :%d' %len(alphabet)
alphabet.pop()
print 'length alphabet :%d' %len(alphabet)

#insert可以指定任意位置insert元素，但是超过当前元素length的时候，只会追加到队尾
alphabet.insert(10,'k')
print 'length alphabet :%d' %len(alphabet)
print 'alphabet[9]:',alphabet[5]

#数组中的元素可以不相同，可以是空，可以list元素中包换list元素，然后组成类似于多维数组的模式
alpha = ['a',100,True]
print 'alpha[2]:',alpha[2]

beta =[alpha,'b',100,True]
print 'beta[0][1]:',beta[0][1]

delta = []
print 'delta length :',len(delta)


#tuple：元祖，类似list，但是一旦初始化就不能再修改了，所以也就没有append,insert此类的方法了，访问方式和list是一样的
#在定义只有元素1的tuple是，会有陷阱，t = (1)表示还没有学到的数学公式，真正的定义一个元素的tuple  需要
t = (1,)
#即使只有一个元素，后面也要跟随一个逗号
t = ('a','b',['c','d'])
t[2][1]='e'
#此时是可以修改成功的，感觉tuple类似于定义指针时使用的const：const char *ptr 意思就是不能通过ptr修改指向的值
