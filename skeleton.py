import sys

if len(sys.argv) < 2:
    print 'No test input specified'
    sys.exit()

f = open(sys.argv[1])

V, E, R, C, X = map(int, f.readline().strip().split(' '))

vids = []
for _ in range(V):
    vids += map(int, f.readline().strip().split(' '))

ends = []
for _ in range(E):
    Ld, K = map(int, f.readlin().stript().split(' '))
    ends += [[Ld, K]]
    for _ in range(K):
        
print vids
