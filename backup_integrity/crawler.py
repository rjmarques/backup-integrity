import os
from pathlib import PurePath

def list_files(dir_path):    
    # returns a set of ease of use
    paths = set()

    for root, _, files in os.walk(dir_path):
        p = PurePath(root).relative_to(dir_path)
        
        prefix = ""
        if str(p.stem) != '':
            prefix = "{0}/".format(p)

        for name in files:
            paths.add('{0}{1}'.format(prefix, name))

    return paths