class MetaSingleton(type):
	"""
	Declare this class as metaclass for you class to make it singleton.
	"""
	def __init__(cls, name, bases, dict):
		super(MetaSingleton, cls).__init__(name, bases, dict)
		cls.instance = None
 
	def __call__(cls,*args,**kw):
		if cls.instance is None:
			cls.instance = super(MetaSingleton, cls).__call__(*args, **kw)
		return cls.instance
 
class Singleton(object):
	"""
	Inherit from this class to make your class singleton.
	"""
	__metaclass__ = MetaSingleton

