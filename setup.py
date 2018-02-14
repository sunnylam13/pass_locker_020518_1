try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Insecure password locker program',
	'author': 'Sunny Lam',
	'url': 'https://github.com/sunnylam13/pass_locker_020518_1',
	'download_url': 'https://github.com/sunnylam13/pass_locker_020518_1',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['sys, pyperclip'],
	'scripts': [],
	'name': 'Password Locker Program Insecure'
}

setup(**config)