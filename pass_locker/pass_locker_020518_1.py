# -*- coding: utf-8 -*-

# ! /usr/local/Cellar/python3/3.6.1

# an insecure password locker program
# ABS:283

PASSWORDS = {
	'email':'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
	'blog':'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
	'luggage':'12345'
}

import sys, pyperclip

if len(sys.argv) < 2:
	print('Usage: python pass_locker_020518_1.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] # first command line arg is the account name

# use `pyperclip.copy()`, from `pyperclip` module

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
	print("There is no account named " + account)

