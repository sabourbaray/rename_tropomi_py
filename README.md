# rename_tropomi_py
Python script to rename SRON TROPOMI files named according to orbit number to append YYYYMMDD to the filenames.

## Instructions

1. Need a previously downloaded TROPOMI dataset that use the NetCDF file structures in the SRON product (such as https://ftp.sron.nl/open-access-data-2/TROPOMI/tropomi/ch4/).
2. Edit "rename_tropomi_py" to modify the path to the directory containing TROPOMI files.
3. Run "python rename_tropomi_py". The script opens each file, reads the YYYYMMDD, and appends to the filename at the end of the orbit number.
4. The new renamed files will be moved to folder "/ncout/".
