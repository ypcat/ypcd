#!/usr/bin/python

import os, sys, re
dirs = sys.stdin.read()[:-1].split('\n')
path = os.path.expanduser(sys.argv[1] or '~')

if path == '-':
    print '-'
    sys.exit(0)
elif path == '-l':
    print>>sys.stderr, '\n'.join(reversed(dirs))
    sys.exit(1)
elif path == '-d':
    h = {}
    for d in dirs:
        v,k = d[:4], d[4:]
        if k in h:
            print v
        h[k] = v
    sys.exit(1)
elif re.match('^\.\.+$', path):
    path = '/'.join(['..']*(len(path)-1))

i,j,d = max((d.find(path), d.find(path)-len(d), d[4:]) for d in dirs)
#print path if os.path.isdir(path) or i < 0 else os.path.expanduser(d)
print (os.path.isdir(path) or i < 0) and path or os.path.expanduser(d)

