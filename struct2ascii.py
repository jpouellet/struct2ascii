#!/usr/bin/env python

import re, string, sys

# How many bits do you want per line?
block = 32

# Do you want to compact giant blocks and mark them with '~'?
compact = True

# Do you want to have the bits counted out at the top?
header = True

# Indent each line with:
ind = '   '

# TODO?
#  - Better handling for fields that extend past the end of a block
#    while not being block-aligned and multiples of a block size.
#    I didn't bother because they're rare enough that I couldn't find
#    an RFC that actually has one as an example of how to do it properly.

exp = r'^\s*%s\s+%s\s*%s\s*;\s*$' % (
	r'u?int(?P<size>[0-9]+)_t',
	r'(?P<name>[_a-zA-Z][_a-zA-Z0-9]*)',
	r'(?:\[\s*(?P<array>[0-9]+)\s*]|)',
)
#print exp
prog = re.compile(exp)

fields = []
for line in sys.stdin:
	#print line
	m = prog.match(line)
	if m is None:
		raise Exception('invalid format: '+line)
	bits = int(m.group('size')) * int(m.group('array') or 1)
	fields.append({'bits': bits, 'name': m.group('name')})

bar = ind+('+-'*block) + '+'
blank_bar = ind+'|' + (' '*(block*2-1)) + '|'
s = ''.join(string.rjust(string.center(f['name'], min(f['bits'],block)*2-1), f['bits']*2-1)+'|' for f in fields)

# header
#print ind+' 0                   1                   2                   3   '
#print ind+' 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 '
if header:
	if bits >= 10:
		print ind+string.ljust('  '+''.join(string.rjust(str(i), 20) for i in xrange(1, block/10+1)), block*2+1)
	print ind+string.ljust(''.join(' '+str(i % 10) for i in xrange(block)), block*2+1)
print bar

skip = 0
while len(s):
	line = s[0:block*2]
	if line == ' '*(block*2):
		skip += 1
	else:
		if skip == 1:
			print ind+'|'+line[:-1]+'|'
			print blank_bar
		elif skip > 0:
			if compact:
				print blank_bar
				print ind+'~'+line[:-1]+'~'
				print blank_bar
			else:
				for i in xrange(skip / 2):
					print blank_bar
				print ind+'|'+line[:-1]+'|'
				for i in xrange(skip - (skip / 2)):
					print blank_bar
		else:
			print ind+'|'+line
		if line[-1] == '|':
			print bar
		skip = 0
	s = s[block*2:]
