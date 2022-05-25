
import os
import sys

ABSPATH=os.path.abspath((sys.argv[0]))
ABSPATH=os.path.dirname(ABSPATH)
print(os.getcwd())

print(ABSPATH)

