# Test data

The 3 folders are an example of a 3-2-1 backup where each folder represents a backup location and should hold all the same files (with the same data). This test data can be used to evaluate multiple components of the service as well as to evaluate the service end-to-end.

The following scenarios are included in the test data:

* good/integral files across backups: binary_1, py_logo.png, text_1
* unique to a *main_backup*: unique.webp
* missing in *secondary_backup*: text_3
* diverging in *tertiary_backup*: text_2