import os
from os import path


class Dir(object):
	@staticmethod
	def walk(root, callback):
		for subitem in os.listdir(root):
			subpath = path.join(root, subitem)
			if path.isdir(subpath):
				Dir.walk(subpath, callback)
			else:
				callback(subpath)


