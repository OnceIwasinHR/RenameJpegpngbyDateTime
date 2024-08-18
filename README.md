# RenameJpegpngbyDateTime python script
Issue: large amount of photos downloaded from icloud, names are messed up and having issue during album creation on local disc.  Solution: use this script to update all names, based on datetime taken+append if multiple taken on same date.
Ensure to update the path where all pictuers are originally extracted in local hard drive. The photos must have date_time parameters with information *can be verified by right click on the downloaded photos - view properties.

If you wish to test it first, i recommend make a extraction into a test folder, with some photos as copy first. Then in main script, update path with test folder. Run it via VSC. Ensure all modules, including python are properly installed first. While the script runs via VSC, in console it will generate names of the files that were renamed, and into the new name as well. if you wish to output the log in file, that can be handled via main code as well. 
