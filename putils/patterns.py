class MetaSingleton(type):
     def __init__(cls, name, bases, dict):
         super(MetaSingleton, cls).__init__(name, bases, dict)
         cls.instance = None
         
     def __call__(cls,*args,**kw):
         if cls.instance is None:
             cls.instance = super(MetaSingleton, cls).__call__(*args, **kw)
         return cls.instance
         
class Singleton(object):
	__metaclass__ = MetaSingleton

