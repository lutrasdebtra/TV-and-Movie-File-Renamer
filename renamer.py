"""
Batch renamer
Stuart Bradley
4/29/2014
"""

import os
import re

test_loc = "/home/stuart/Code/Renamer/Test Structure"

files_to_change = '*.avi' 

for root, dirnames, filenames in os.walk(test_loc):
	print root
	print dirnames
	print filenames

"""
for f in glob2.glob(test_loc + '/**/*'):
		if re.search('S\d+E\d+', f):
			print 'Already in S##E## format - Skipping'
			continue
		else:
			titleArray = f.split()
			season = titleArray[6]
			episode = titleArray[8]
			f2 = 'Two And A Half Men - S' + season + 'E' + episode + '.avi'
        	print 'renaming: ', f, ' -> ', f2
        	os.rename(f, f2) 
print 'All Done' 
"""
