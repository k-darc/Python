import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])

# Run python say.py name e.g. python say.py world