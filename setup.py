from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "putils",
    version = "0.2.1",
    author = "Stanislav Feldman",
    description = ("Python utils"),
    url = "https://github.com/stanislavfeldman/putils",
    keywords = "utils singleton dict ternary filesystem",
    packages=['putils'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Software Development"
    ],
)
