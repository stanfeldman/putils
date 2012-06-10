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
	def __new__(cls, **enums):
		return type('Enum', (), enums)
		
		
class Struct(object):
	"""
	Dict to object conversion.
	"""
	def __init__(self, **entries): 
		self.__dict__.update(entries)

