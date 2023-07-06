from dataclasses import dataclass

@dataclass
class IntegrityReport:
    """Class containing the integrity report for the backup locations."""
    
    # list of files that are present across all backups and are valid
    valid: list
    # files that are different across pairs of backups: file -> [(backup_x, backup_y), (backup_x, backup_z)]
    invalid: dict
    # files that are missing in specific backups: file -> [backup_w, backup_z]
    missing: dict

    def export_to_file(self, report_path, export_valid=False):
        with open(report_path, "w") as report_file:
            # write all missing files
            # report_file.writelines(["Hey there!", "LearnPython.com is awesome!"])
            report_file.write("------------------ Missing files ------------------\n")
            for f, dirs in self.missing.items():
                 report_file.write("{0} missing from:\n".format(f))
                 for d in dirs:
                     report_file.write("    * {0}\n".format(d))
            
            # write all invalid files
            report_file.write("\n------------------ Invalid files ------------------\n")
            for f, dir_pairs in self.invalid.items():
                report_file.write("{0} diverging between:\n".format(f))
                for (back_a, back_b) in dir_pairs:
                    report_file.write("    * {0} and {1}:\n".format(back_a, back_b))

            # write all valid files
            if export_valid:
                report_file.write("\n------------------ Valid files ------------------\n")
                for f in self.valid:
                    report_file.write("{0}\n".format(f))
