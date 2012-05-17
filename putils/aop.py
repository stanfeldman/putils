from __future__ import absolute_import
from types import TypeType
import re


class AspectCall(object):
	def __init__(self, func, aspect):
		self.func = func
		self.aspect = aspect
	def __call__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		self.aspect.on_enter(self)
		try:
			self.result = self.func(*self.args, **self.kwargs)
			self.aspect.on_success(self)
			return self.result
		except Exception, e:
			self.exception = e
			self.aspect.on_fail(self)

	
class Aspect(object):
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
