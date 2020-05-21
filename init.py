import os
import sys

print("Starting...\n")

for i in range(0, int(sys.argv[1])):
    print("{0}/{1}".format(i, sys.argv[1]))
    os.system("python main.py")
