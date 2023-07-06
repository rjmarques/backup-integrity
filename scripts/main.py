#inside <root>/scripts/main.py
import os
import sys

from backup_integrity import Controller

def main():
    args = sys.argv[1:]
    dir_paths = [os.path.abspath(path) for path in args]

    validate_args(dir_paths)

    ctrl = Controller(dir_paths)
    out = ctrl.verify_file_integrity()

    print(out.pretty_print())

def validate_args(args):
    if len(args) <= 1:
        sys.exit("error -> expected at least two target folders but got {0}: {1}".format(len(args), args[0]))

    for idx, x in enumerate(args):
        next = idx+1
        for y in args[next:]:
            common = os.path.commonpath([x, y])
            if common == x or common == y:
                sys.exit("error -> {0} and {1} collide. Please provide independent base directories".format(x, y))

if __name__ == "__main__":
    main()