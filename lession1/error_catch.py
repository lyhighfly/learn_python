#!/usr/bin/env python
#coding=utf-8

import logging
class ErrorCatch(object):

	def fun(self):

		try:
			#do something
#有很多种Exception，都是继承自BaseException,StandardError就是Error的统称，如果except还有其他error，则不会到达，全部交由StandardError处理
		except: StandardError, e:
			logging.exception(e)
			raise
#raise 可以不带参数的原样将当前错误抛给上层去处理
		finally:
			#do final things

#不同于java，在需要catch的地方，必须catch，或者throws exception，python 会自动catch 多层调用中的Error，不需要在可能Error的地方都声明try except，或者throws可能的错误



#如果error没有except的地方，最后会交由python解释器，最后所有信息都写入err.py文件，可以使用python err.py进行查看

#可以使用assert进行异常处理，抛出AssertionError，并停止运行，相较print的好处就是，可以使用python命令将assert屏蔽掉
#logging则不会暂停，之后记录结果
#pdb方式单步调试

#单元测试，跳过
