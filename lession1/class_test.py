#!/usr/bin/env python
#coding=utf-8

import types
from types import MethodType
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
		self._name = name
		self.age = age
#据说 __param的变量 是private的，外部不能方位，but  貌似可以直接访问，如下所示；__param__的变量为特殊变量，外界可以直接访问
#all method first param must be self
	def print_namea(self):
		print 'student name',self._name
#__init__貌似只能有一个，跟java中可以有多个不同参数的构造器不同，貌似这样不会报错，但是构造器只取最后一个__init__的签名
	#def __init__(self, name):
	#	self.name = name

#如果没有 构造函数__init__，则不能在create instance的时候，传递任何参数
student1 = StudentPro('lll', 10)
student1.age = 20
student1._name = 'ly'
print student1._name, student1.age

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




#以下是动态语言的残暴技能
#1,属性的动态绑定
s = StudentPro('kk',25)
s.height = 111
print 'Student s height:',s.height

#2,残暴技能，方法绑定，将自定义方法，绑定到实例，只对绑定的实例有效，新的对象实例不具有绑定方法
def set_height(self,height):
	self.height = height

#如果把MethodType中的s 换成None，就是对对象本身的绑定，以后创建的所有对象实例都会有绑定的方法
s.set_height = MethodType(set_height, s, StudentPro)
s.set_height(200)

print 'Student s height:',s.height


#3,残暴收敛技能，限定绑定属性

class Teacher(object):
#使用__slots__ + tuple  将绑定属性限制为有限类型，如果超过限制，则会报：AttributeError：has no attribute
	__slots__ = ('name','height')

#此技能只对当前类起作用，子类不受父类中__slots__的限制
teacher = Teacher()
teacher.name = 'wow'
teacher.height = 188
teacher.weight = 90


#4,Property技能先跳过吧 :P


#5,python支持多继承概念，一条主线，附加功能也作为父类继承给子类，这种设计叫做Mixin，在python很常见

class Humen(Teacher,Student):
	pass
#当然，上例是不合理的，只是作为演示，表示可以同时继承多个父类

#6,类的定制功能
#__slots__用于限定绑定属性
#__len__
#__str__like  java toString()
#__iter__  用于迭代，同时实现next(self)方法，这样就可以使用for in 进行迭代了
#__getitem__ 用于是其可以像list一样，使用下标进行访问，调用返回下标对应的值，可以做到支持slice功能
#__getattr__  容错吧，就是在获取错误的属性时，根据具体情况作出处理
#__call__  用于相应实例调用自身的返回结果：instance()



#7,可以使用type进行class的动态创建，这个功能更残暴，我去动态创建class,这就四动态语言相较静态语言的不同
#8，metaclass的使用，跳过吧


