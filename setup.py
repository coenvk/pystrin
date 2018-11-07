import setuptools


with open('README.md', 'r') as fh:
	long_description = fh.read()


setuptools.setup(
	name='pystrin',
	version='0.0.6',
	author='Coen van Kampen',
	author_email='c.m.vankampen14@gmail.com',
	description='A small Python package used for string interpolation',
	long_description=long_description,
	url='https://github.com/campoe/pystrin',
	packages=setuptools.find_packages(),
	license='MIT',
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)