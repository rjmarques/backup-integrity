import os
from collections import defaultdict
from .crawler import list_files
from .results import IntegrityReport
from .integrity import compare

class Controller():
    def __init__(self, dir_paths):
        self.dir_paths = dir_paths

    def verify_file_integrity(self):
        valid = []
        invalid = defaultdict(list)
        missing = defaultdict(list)
        
        # collect all files from each target directory 
        files_by_backup = self.files_by_folder()

        # files already processed
        processed = set()

        # iterate over all files, comparing all backups to one another
        for root_dir, files in files_by_backup:
            # gather other backups excluding the main we're iterating
            other_backups = [ (key,value) for key, value in files_by_backup if root_dir != key ]
            
            for f in files:
                if f in processed:
                    continue
                
                validated = True
                file_path = os.path.join(root_dir, f)

                for other_root, other_files in other_backups:
                    if not f in other_files:
                        missing[f].append(other_root)
                        validated = False
                        continue

                    other_path = os.path.join(other_root, f)
                    
                    # compare files
                    equal = compare(file_path, other_path)
                    if not equal:
                        invalid[f].append((root_dir, other_root))
                        validated = False

                if validated:
                    valid.append(f)

                processed.add(f)

        return IntegrityReport(valid, dict(invalid), dict(missing))
    
    def files_by_folder(self):
        res = []

        for path in self.dir_paths:
            res.append((path, list_files(path)))

        return res
    