#! python3
# pw.py - An insecure password locker program

passwords = {
'email': 'ayush5555555',
'fb': 'ssiudsi889',
'orkut': 'shssd$$222',
}

import sys, pyperclip
if (len(sys.argv) < 2):
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]  #first command line arg is the account name

if account in passwords:
	pyperclip.copy(passwords[account])
	print('password for ' + account + ' is copied to the clipboard')
else:
	print('You don\'t have an account named ' + account)
