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

    def pretty_print(self) -> str:
        # TODO
        return "foo-bar"