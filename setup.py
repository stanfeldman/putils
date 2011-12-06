from distutils.core import setup
try:
	from setuptools import setup
except:
	pass

setup(
    name = "putils",
    version = "0.0.1",
    author = "Stanislav Feldman",
    description = ("Python utils"),
    keywords = "utils singleton dict ternary",
    packages=['putils'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development"
    ],
)
