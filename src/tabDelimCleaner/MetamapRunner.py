import os
import shutil
import subprocess


def metamapRun(fileDir, metamapLoc, WSD, JSON):
    """
    :param fileDir: The location of the folder holding all files to be passed to metamap
    :param metamapLoc: The local location of your metamap file, all the way up to the slash before public_mm. Don't include slash.
    :param WSD: True or false. True means the program will run with WSD active, False means it won't.
    :param JSON: True or false. True means the program will return a JSON file, False means it returns a human readable.
    :return: returns location of output file folder.

    Human readable files take far longer to write than JSON files, and WSD takes longer than no WSD.
    Fastest way to run would likely be: fileDir metamapLoc False True
    """
    # Attempts to make a list of every file directory in the given folder
    files = os.listdir(fileDir)

    # Makes an output folder in the given folder if it isn't already there, adds () info for clarification reasons
    if WSD & JSON:
        outputLoc = os.path.join(fileDir, "metamapOutput (WSD + JSON)")
        if not os.path.isdir(outputLoc):
            os.mkdir(outputLoc)
    elif WSD:
        outputLoc = os.path.join(fileDir, "metamapOutput (WSD)")
        if not os.path.isdir(outputLoc):
            os.mkdir(outputLoc)
    elif JSON:
        outputLoc = os.path.join(fileDir, "metamapOutput (JSON)")
        if not os.path.isdir(outputLoc):
            os.mkdir(outputLoc)
    else:
        outputLoc = os.path.join(fileDir, "metamapOutput")
        if not os.path.isdir(outputLoc):
            os.mkdir(outputLoc)

    # Starts metamap
    subprocess.run(metamapLoc + "/public_mm/bin/skrmedpostctl start", shell=True)
    # Starts WSD server if given true
    if WSD:
        subprocess.run(metamapLoc + "/public_mm/bin/wsdserverctl start", shell=True)

    # tries to run metamap on each file, returns number of files left to run so that I don't go insane
    remaining = len(files)
    created = 0
    for i in files:
        # Creates directories for command to refrence
        newDir = fileDir + "/" + i
        outFileName = i + ".out"
        # Checks if the file already exists, if it does then skips to the next file; helps user recover from crashes
        # (I need to make this work for all parts of pipeline)
        if os.path.isfile(outputLoc + "/" + outFileName):
            continue
        # runs different commands based on whether WSD and JSON are true or not
        if WSD & JSON:
            metamapCommand = metamapLoc + "/public_mm/bin//metamap -I -y --JSONn " + newDir
        elif WSD:
            metamapCommand = metamapLoc + "/public_mm/bin//metamap -I -y " + newDir
        elif JSON:
            metamapCommand = metamapLoc + "/public_mm/bin//metamap -I --JSONn " + newDir
        else:
            metamapCommand = metamapLoc + "/public_mm/bin//metamap -I " + newDir
        # Tries to run the command to make metamap run
        subprocess.run(metamapCommand, shell=True)
        created += 1
        remaining -= 1
        print(str(remaining) + " files remaining.")

    # Writes progress to log file by patient
    log = open("log.txt", "a")
    if WSD & JSON:
        outType = " WSD + JSON"
    elif WSD:
        outType = " WSD"
    elif JSON:
        outType = " JSON"
    else:
        outType = " default"
    log.write(str(created) + outType + " metamap output files created for patient " +
              (files[0])[(files[0]).find("_") + 1: (files[0]).find(".")] +
              " (if restarting after an error, don't worry about created file count.)\n")
    log.close()

    # Refreshes files list, Should manually transfer the output files to metamap output folder
    files = os.listdir(fileDir)
    for i in files:
        if i[len(i)-3:len(i)] == "out":
            oldFile = os.path.join(outputLoc, i)
            shutil.move(os.path.join(fileDir, i), oldFile)
            if JSON:
                # Renames moved file to .json
                os.rename(oldFile, oldFile[0:oldFile.find(".") + 1] + "json")
            else:
                # Renames moved file to .mmout (metamap output)
                os.rename(oldFile, oldFile[0:oldFile.find(".") + 1] + "mmout")

    # Closes metamap for the sake of consistency and my minor OCD.
    subprocess.run(metamapLoc + "/public_mm/bin/skrmedpostctl stop", shell=True)
    # Closes WSD server
    if WSD:
        subprocess.run(metamapLoc + "/public_mm/bin/wsdserverctl stop", shell=True)
    # returns location of output file folder
    return outputLoc
