import sys

if len(sys.argv) < 2:
    print 'No test input specified'
    sys.exit()

f = open(sys.argv[1])
for l in f:
    print l
