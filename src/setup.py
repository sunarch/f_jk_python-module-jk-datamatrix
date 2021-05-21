################################################################################
################################################################################
###
###  This file is automatically generated. Do not change this file! Changes
###  will get overwritten! Change the source file for "setup.py" instead.
###  This is either 'packageinfo.json' or 'packageinfo.jsonc'
###
################################################################################
################################################################################


from setuptools import setup

def readme():
	with open("README.md", "r", encoding="UTF-8-sig") as f:
		return f.read()

setup(
	author = "Jürgen Knauth",
	author_email = "pubsrc@binary-overflow.de",
	classifiers = [
		"Development Status :: 3 - Alpha",
		"License :: OSI Approved :: Apache Software License",
		"Programming Language :: Python :: 3",
	],
	description = "This python module provides a class that represents a data matrix. This is basically a table you can work with: Modify, sort, filter and print. Everthing is kept in memory, is not indexed, and therefore intended for a limited amount of data only.",
	include_package_data = False,
	install_requires = [
		"jk_console",
	],
	keywords = [
		"matrix",
		"table",
		"data",
		"datatable",
	],
	license = "Apache2",
	name = "jk_datamatrix",
	packages = [
		"jk_datamatrix",
	],
	version = "0.2021.5.21",
	zip_safe = False,
	long_description = readme(),
	long_description_content_type="text/markdown",
)
