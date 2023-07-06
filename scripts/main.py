#inside <root>/scripts/main.py
import os
import errno
import sys
import argparse

from backup_integrity import Controller

def main():
    dir_paths, target_output = process_args()

    ctrl = Controller(dir_paths)
    out = ctrl.verify_file_integrity()

    out.export_to_file(target_output, export_valid=True)

def process_args():
    parser = argparse.ArgumentParser(description='Validate files between backup directories that should have exactly the same contents', usage='%(prog)s [-h] directory_1 directory_2 [directory_N ...]')
    parser.add_argument('directory_1', nargs=1, metavar='directory_1')
    parser.add_argument('directory_n', nargs='+', metavar='directory_2')
    parser.add_argument('--output', metavar="./my/outputs/report.txt", default="./report.txt", help='Report file path (including file name)')

    args = parser.parse_args()

    dir_paths = [os.path.abspath(path) for path in args.directory_1 + args.directory_n]

    if len(dir_paths) <= 1:
        sys.exit("error -> expected at least two target folders but got {0}: {1}".format(len(dir_paths), dir_paths[0]))

    for idx, x in enumerate(dir_paths):
        if not os.path.exists(x):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), x)

        next = idx+1
        for y in dir_paths[next:]:
            common = os.path.commonpath([x, y])
            if common == x or common == y:
                sys.exit("error -> {0} and {1} collide. Please provide independent base directories".format(x, y))

    return (dir_paths, args.output)

if __name__ == "__main__":
    main()