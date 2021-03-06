import os
import imp
import sys
import mimetypes
import inspect


class Importer(object):
	"""
	Use methods of this class to import class or module
	"""
	@staticmethod
	def import_class(cl):
		"""
		Imports class by name
		"""
		d = cl.rfind(".")
		classname = cl[d+1:len(cl)]
		m = __import__(cl[0:d], globals(), locals(), [classname])
		return getattr(m, classname)
		
	@staticmethod
	def import_module(module):
		"""
		Imports module by name
		"""
		d = module.rfind(".")
		modulename = module[d+1:len(module)]
		mod = __import__(module, globals(), locals(), [modulename])
		return mod
		
	@staticmethod
	def module_path(module):
		"""
		Returns path of module
		"""
		result = os.path.dirname(Importer.import_module(module).__file__)
		return result
		
	@staticmethod
	def object_path(obj):
		"""
		Returns path of module which contains class of this object
		"""
		result = inspect.getmodule(obj).__file__
		return result
		
	@staticmethod
	def import_module_by_path(filepath):
		"""
		Imports module by path
		"""
		for base_path in sys.path:
			try:
				filepath = os.path.relpath(filepath, base_path)[:-3]
				module_name = '.'.join(filter(None, filepath.replace('.', '').split('/')))
				return Importer.import_module(module_name)
			except:
				pass
		return None
			
	

class Introspector(object):	
	@staticmethod
	def classname(obj, full=True):
		"""
		Returns full qualified class name
		"""
		if inspect.isclass(obj):
			cname = obj.__name__
		else:
			cname = obj.__class__.__name__
		if full:
			return obj.__module__ + "." + cname
		else:
			return cname
		
	@staticmethod
	def all_subclasses(cls):
		result = set()
		for sub in cls.__subclasses__():
			result.add(sub)
			result.update(Introspector.all_subclasses(sub))
		return list(result)
		
	@staticmethod
	def class_that_defined_method(meth):
		obj = meth.im_self
		for cls in inspect.getmro(meth.im_class):
			if meth.__name__ in cls.__dict__:
				return cls
		return None
		
	@staticmethod
	def baseclass_before(cls, before_cls):
		"""
		returns base class in base classes chain before some class
		"""
		last = None
		for c in inspect.getmro(cls):
			if c is not before_cls:
				last = c
			else:
				break
		return last
		
	@staticmethod
	def baseclasses_before(cls, before_cls):
		"""
		returns base classes in base classes chain before some class
		"""
		result = []
		for c in inspect.getmro(cls):
			if c is not before_cls:
				if c is not cls:
					result.append(c)
			else:
				break
		return result
        
