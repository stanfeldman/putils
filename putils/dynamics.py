import os


class Importer(object):
	@staticmethod
	def import_class(cl):
		d = cl.rfind(".")
		classname = cl[d+1:len(cl)]
		m = __import__(cl[0:d], globals(), locals(), [classname])
		return getattr(m, classname)
		
	@staticmethod
	def import_module(module):
		d = module.rfind(".")
		modulename = module[d+1:len(module)]
		mod = __import__(module, globals(), locals(), [modulename])
		return mod
		
	@staticmethod
	def module_path(module):
		result = os.path.dirname(Importer.import_module(module).__file__)
		return result
