import os


class Dict(object):
	@staticmethod
	def flat_dict(d, delimiter="/", start_char="^", end_char="$", key="", out={}):
		for k,v in d.iteritems():
			new_key = key + delimiter + k
			if isinstance(v, dict):
				Dict.flat_dict(v, delimiter, start_char, end_char, new_key, out)
			else:
				out[start_char + new_key + end_char] = v
		return out
		
	@staticmethod
	def merge(d1, d2):
		for k1,v1 in d1.iteritems():
			if not k1 in d2:
				d2[k1] = v1
			elif isinstance(v1, dict):
				Dict.merge(v1, d2[k1])
		return d2

		
class Boolean(object):
	@staticmethod
	def ternary(cond, t, f):
		return (cond and [t] or [f])[0]
		

class Enum(object):
	def __new__(cls, **enums):
		return type('Enum', (), enums)

