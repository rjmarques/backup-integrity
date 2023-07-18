import os
from time import sleep
from collections import defaultdict
from tqdm import tqdm
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
            print("processing files in '{0}'".format(root_dir))

            # gather other backups excluding the main we're iterating
            other_backups = [ (key,value) for key, value in files_by_backup if root_dir != key ]
            
            for f in tqdm(files, unit='files'):                
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
                    if not self.isEqual(file_path, other_path):
                        invalid[f].append((root_dir, other_root))
                        validated = False

                if validated:
                    valid.append(f)

                processed.add(f)

        return IntegrityReport(valid, dict(invalid), dict(missing))
    
    def isEqual(self, file_a, file_b, max_retry=5):
        for _ in range(max_retry):
            try:
                return compare(file_a, file_b)
            except (RuntimeError, OSError) as err:
                 print("error comparing {0} to {1}: {2}".format(file_a, file_b, err))
                 # wait a bit to see if the IO issue disappears
                 sleep(1)
        
        # if it reaches here it was not able to compare the files!
        raise RuntimeError("too many errors...aborting") 


    def files_by_folder(self):
        res = []

        for path in self.dir_paths:
            print("crawling through '{0}' to collect files".format(path))
            res.append((path, list_files(path)))

        return res
    