from DelimToText import delimToTxt
from MetamapRunner import metamapRun
from JSONparser import reader, grader

# Runs delim to text on cage, returns folder location
# Runs metamap on each folder's files, returns directory of folder.
# Reads metamap output, returns directory of read files
# Turns returned Json files into CSV result files
# Grades all returned JSON files

# Shoved in one line, because why not? Hate me if you want, but it's easy enough to change if done from the outside in.
grader(reader(metamapRun(delimToTxt("Clinical Skills Notes 2022 De-ID.xlsx - Clinical Skills_3.17.22.tsv", "Cage"), "/home/em-is-an-em/Desktop", True, True)), "/home/em-is-an-em/PycharmProjects/tabDelimCleaner/CompareAgainst.txt", 100)
# Runs metamap to create human readable files
metamapRun("/home/em-is-an-em/PycharmProjects/tabDelimCleaner/PatientData/CageData", "/home/em-is-an-em/Desktop", True, False)
