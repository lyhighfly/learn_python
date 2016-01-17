#!/usr/bin/env python
#coding=utf-8

'test for module ues'

__author__ = 'liuyu'

import sys

def test():
#sys.argv中包含所有的参数信息，类似c
	args = sys.argv
	if len(args) == 1:
		print 'arg is %s' %args[0]
	elif len(args) == 2:
		print 'arg %s value %s' %(args[0],args[1])
	else:
		print 'too many params'

#此py单独启动时，name = 'main' 如果是import，则!= ,常用于但愿测试
if __name__ == '__main__':
	test()


#__params__:常用于特殊用途
#params :public
#__params:private

#pip install PIL 暂时没有成功，先跳过吧
