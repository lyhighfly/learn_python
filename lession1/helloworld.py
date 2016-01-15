#!/usr/bin/env python
#coding=utf-8  
#必须加上编码格式，才能在代码文件中添加中文内容
#添加完上述一行之后，然后更改本文件的执行权限，就可以直接./helloworld.py来运行本demo了
print 'hello world from python'
#可以使用，将多个语句链接，逗号算一个空格，空格本身不算空格
print 'hello world','from',"python"
#inputCount = raw_input,用于从终端读入输入，以回车键结束 也可以使用raw_input(tips)用于提示用户输入内容
name=raw_input()
print 'input name=',name
#大小写敏感 Name != name

#缩进代表代码块，以：表示代码块的开始
value = 9
if value < 10:
	print 'value is lower than 10'
else:
	print 'value is great than 10'

#转义符的用法和c java 是相同的，不过这里有个特殊用法  r'\\n\n'  表示引号中的不用转义
print r'\\\n\n'

#py内置了布尔值(打印出来的也是True,False ,跟c不一样)，True False , 布尔预算则是：and or not 法则是通用的

print True
print False
print True and False
print True or False
print not False

#None代表空值，不同于0值
print 'None =',None

#py 中没有变量类型概念，所以，可以同一变量反复赋值，赋予不同类型的值
#这也就是动态语言和静态语言的不同之处
param = 'abc'
param = 123
print 'param = ',param

#同样的，py 也是将常量大写表示的，但是没有如同const  final一类的保护机制，所以维护工作要自己做
PI=3.1415926
