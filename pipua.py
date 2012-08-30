#!/usr/bin/env python
import subprocess
commands = ['pip', 'install', '--upgrade']
blacklist = ['gitup']
def main():
	global commands
	res = subprocess.check_output(['pip', 'freeze'])
	split = res.split('\n')
	for line in split:
		if line.startswith('-e'):
			continue
		name = line[:line.find('==')]
		if not name.isspace() and name and not (name in blacklist):
			commands.append(name)
	subprocess.call(commands)

main()
