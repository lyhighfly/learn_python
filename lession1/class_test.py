#!/usr/bin/env python
#coding=utf-8

import types
#（）内的为Student的父类，一般没有明确父类的时候，可以使用object
class Student(object):
	pass

student = Student()

print student
#wocao,可以自由的给类实例去绑定之前没有的属性，这能力也太残暴了吧。。。
student.name = 'll'
print student.name

class StudentPro(Student):
#构造函数的第一项必须是self，创建instance的时候，self是不用传递的
	def __init__(self, name, age):
		self.__name = name
		self.age = age
#据说 __param的变量 是private的，外部不能方位，but  貌似可以直接访问，如下所示；__param__的变量为特殊变量，外界可以直接访问
#all method first param must be self
	def print_namea(self):
		print 'student name',self.__name
#__init__貌似只能有一个，跟java中可以有多个不同参数的构造器不同，貌似这样不会报错，但是构造器只取最后一个__init__的签名
	#def __init__(self, name):
	#	self.name = name

#如果没有 构造函数__init__，则不能在create instance的时候，传递任何参数
student1 = StudentPro('lll', 10)
student1.age = 20
student1.__name = 'ly'
print student1.__name, student1.age

print student1.print_namea()


#以下是继承，多态

class Animals(object):

	def __init__(self,species):
		self.specices = species
	
	def run(self):
		print 'animals is running'

class Dog(Animals):

#child 如何在初始化时调用parent的初始化函数的super方式，一直没有想通，感觉和java一点都不一样啊啊啊啊啊啊
	def __init__(self, color):
	#	super(Dog).__init__(Animals,'a')
		Animals.__init__(self,'a')
		self.color = color
	
	def run(self):
		print self.specices,self.color,' dog is running'


dog = Dog('Black')
dog.run()
#对于继承关系，使用type是得不到正确的结果的
print type(dog) == type(Animals)
print isinstance(dog, Animals)

#如果父类的的初始化函数，不只有一个self(非默认初始化)，则子类在继承父类的时候，必须也显示的初始化，并调用父类的初始化
class FooParent(object):

	def __init__(self,name):

		self.parent = 'I`m from parent',name
		print 'Parent'

	def bar(self, message):
		print message,'from Parent'

class FooChild(FooParent):

	def __init__(self):

		FooParent.__init__(self,'haha')
		print 'Child'

	def bar(self, message):

		FooParent.bar(self,message)
		print 'Child`s function'
		print self.parent

child = FooChild()
child.bar('HelloWorld')

