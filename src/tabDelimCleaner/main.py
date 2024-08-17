from DelimToText import delimToTxt, getPatients
from MetamapRunner import metamapRun
from JSONparser import reader, grader

"""
IMPORTANT INFO (Updated 8/1/22):
Try to restart computer before running pipeline. 
Restarting seems to mitigate metamap errors, though I can't be certain if that's really the case.
Remember to delete or move all files created by this program before rerunning the pipeline. 
If files already exist, different steps of the pipeline will react differently.

Delim to text ignores CSV lines with the same patient and the same timestamp.

You MUST start metamap servers in the command line before running metamapRunner

Metamap itself errors out sometimes. Expect JSON truncation and/or empty files.
Json reader creates both a 2d array and a dictionary. 
The 2d array is used to make a CSV file, while the dictionary is currently unused.
"""

# Gets all patient names from CSV files and returns an array of them
patients = getPatients("out")
# Makes a list of the names of all folders created while running program
folderDirs = []
# Runs delim to text on each patient, returns directory each created folder
for i in patients:
    folderDirs.append(delimToTxt("out", i))

# Runs metamap on each folder's files, returns directories of each folder.
allMMOutput = []
for i in folderDirs:
    allMMOutput.append(metamapRun(i, "/home/em-is-an-em/Desktop", True, True))

# Reads metamap output and converts to csv, returns output directory.
# Also creates a dictionary that isn't used right now.
CSVs = []
for i in allMMOutput:
    CSVs.append(reader(i))

# Runs the grader on each file
for i in CSVs:
    grader(i, "/home/em-is-an-em/PycharmProjects/tabDelimCleaner/CompareAgainst.txt", 100)
