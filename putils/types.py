import os


class Dict(object):
	"""
	Dict utils.
	"""
	@staticmethod
	def flat_dict(d, delimiter="/", start_char="^", end_char="$", key="", out={}):
		"""
		Flats hierarhical dict.
		"""
		for k,v in d.iteritems():
			new_key = key + delimiter + k
			if isinstance(v, dict):
				Dict.flat_dict(v, delimiter, start_char, end_char, new_key, out)
			else:
				out[start_char + new_key + end_char] = v
		return out
		
	@staticmethod
	def merge(d1, d2):
		"""
		Deep merge of two dicts.
		"""
		for k1,v1 in d1.iteritems():
			if not k1 in d2:
				d2[k1] = v1
			elif isinstance(v1, list):
				d2[k1] = d2[k1] + v1
			elif isinstance(v1, dict):
				Dict.merge(v1, d2[k1])
		return d2

		
class Boolean(object):
	@staticmethod
	def ternary(cond, t, f):
		"""
		Use it if you need ternary operator
		"""
		return (cond and [t] or [f])[0]
		

class Enum(object):
	"""
	Creates enum.
	"""
	def __init__(self, **enums):
		self.__dict__ = enums
		self._enums = enums
		
	def get(self, name):
		return self._enums[name]
		
	def get_by_value(self, value):
		if not self.has_value(value):
			raise LookupError("Enum does not contain value %s" % value)
		return value
		
	def has_value(self, value):
		return value in self._enums.values()
		
	def has_key(self, key):
		return key in self._enums.keys()
		
		
class Struct(object):
	"""
	Dict to object conversion.
	"""
	def __init__(self, **entries): 
		self.__dict__.update(entries)
		
		
class Regex(object):
	"""
	Various regex utils
	"""
	@staticmethod
	def string_url_regex(str_name):
		"""
		Returns regex for url mapping with sting param
		"""
		return r"""(?P<%s>[^ \,\:\;\"\\/']+)""" % str_name
		
	@staticmethod
	def number_url_regex(num_name):
		"""
		Returns regex for url mapping with int param
		"""
		return r"""(?P<%s>\d+)""" % num_name

