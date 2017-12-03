from setuptools import setup

setup(
	name='clienc',
	version=0.1,
	py_modules=['clienc'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		clienc=clienc:cli
		''',
)
