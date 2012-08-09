import os
import imp


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
	def import_module_by_path(filepath):
		"""
		Imports module by path
		"""
		mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])
		if file_ext.lower() == '.py':
			py_mod = imp.load_source(mod_name, filepath)
		elif file_ext.lower() == '.pyc':
			py_mod = imp.load_compiled(mod_name, filepath)
		return py_mod
	

class Introspector(object):	
	@staticmethod
	def all_subclasses(cls, result=[]):
		for sub in cls.__subclasses__():
			result.append(sub)
			Introspector.all_subclasses(sub, result)
		return result
        
