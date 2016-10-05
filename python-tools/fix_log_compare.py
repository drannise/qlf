import sys
import os


def usage():
    print("Usage: %s <file1> <file2>" % os.path.basename(__file__))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
        exit()

    file1 = sys.argv[1]
    file2 = sys.argv[2]
