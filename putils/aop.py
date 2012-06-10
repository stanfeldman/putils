from __future__ import absolute_import
from types import TypeType
import re


class AspectCall(object):
	"""
	This object will be passed to methods of your aspect.
	"""
	def __init__(self, func, aspect):
		self.func = func
		self.aspect = aspect
	def __call__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		on_enter_result = self.aspect.on_enter(self)
		if on_enter_result:
			return on_enter_result
		try:
			self.result = self.func(*self.args, **self.kwargs)
			on_success_result = self.aspect.on_success(self)
			if on_success_result:
				return on_success_result
			return self.result
		except Exception, e:
			self.exception = e
			on_fail_result = self.aspect.on_fail(self)
			if on_fail_result:
				return on_fail_result

	
class Aspect(object):
	"""
	You need to inherit from this class to create your own aspect.
	Then you can declare decorator of class or function with this aspect like this: @Aspect()
	"""
	def __init__(self, filter=""):
		self.filter = re.compile(filter)
		
	def __call__(self, cls):
		return self.wrap(cls)
		
	def wrap(self, wrapped):
		parent = self
		parent_filter = self.filter
		if wrapped.__class__ == TypeType:
			class Wrapper(object):
				def __init__(self, *args, **kwargs):
					self.wrapped = wrapped(*args, **kwargs)
				def __getattr__(self, name):
					func = getattr(self.wrapped, name)
					if not parent_filter or parent_filter.match(name):
						return AspectCall(func, parent)
					else:
						return func
			return Wrapper
		else:
			def wrapper(*args, **kwargs):
				func = wrapped
				name = wrapped.__name__
				if not parent_filter or parent_filter.match(name):
					return AspectCall(func, parent)(*args, **kwargs)
				else:
					return func(*args, **kwargs)
			return wrapper
		
	def on_enter(self, call):
		pass
		
	def on_success(self, call):
		pass
		
	def on_fail(self, call):
		pass
