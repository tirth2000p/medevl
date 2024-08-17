import os

def delimToTxt(fileDir, patient):
    """
    :param fileDir: The name of the TAB DELIMITED FILE (must be .tsv format) to be read
    :param patient: The name of the patient to take information on
    :return: The directory of the folder that holds all created text files
    """
    # Creates array to store data
    data = []
    # open .tsv file
    with open(fileDir) as f:
        # Read data line by line
        for line in f:
            # splits data by tab, will store it in list if it's for the right patient
            listItem = line.split('\t')
            if listItem[2] == patient:
                data.append(listItem)
    # closes file
    f.close()

    # Gets the current directory. If there is no patient data folder, creates it
    directory = os.path.join(os.getcwd(), "PatientData")
    if not os.path.isdir(directory):
        os.mkdir(directory)
    # Makes a folder in patient data folder, then creates a string that holds the current file directory
    os.mkdir(os.path.join(directory, patient + "Data"))
    directory = directory + "/" + patient + "Data/"

    # Removes duplicate patient data entries based on timestamp
    duplicates = 0
    # "i" is the index. This isn't a for loop because the length of the data list, aka end, changes.
    i = 0
    end = len(data) - 1
    while i < end:
        while True:
            if (data[i][1] == data[i + 1][1]) & (data[i][0] == data[i + 1][0]):
                del data[i+1]
                duplicates += 1
                end -= 1
            else:
                break
        i += 1

    # evaluates each line and places it in a new file, counting each occurrence
    count = 0
    skipped = 0
    for i in data:
        # creates new file with array data
        # runs a try catch with the make folder. if it fails, assumes it's failing because file already exists
        try:
            file = open(directory + i[1] + "_" + i[2] + ".txt", "x")
            file.write(i[3])
            file.close()
            count += 1
        # adds a 1 to the end of the current file and tries again. if that fails, assumes there's a 1 on an earlier file
        except:
            try:
                file = open(directory + i[1] + "_" + i[2] + "1.txt", "x")
                file.write(i[3])
                file.close()
                count += 1
            # Tries to get the newest int ending for this file name and increment it up one,
            # then attaches int to the end and makes a new file with that.
            except:
                # Uses Error Ending because something'd be really wrong if it appeared
                ending = "Error"
                skip = False
                # There'd better not be more than 100 by the same person on the same person
                for x in range(1, 101):
                    if not os.path.isfile(directory + i[1] + "_" + i[2] + x):
                        ending = x
                        break
                    # if all else fails, skip and increment skipped by one
                    if x == 100:
                        skip = True
                        skipped += 1
                if not skip:
                    file = open(directory + i[1] + "_" + i[2] + ending + ".txt", "x")
                    file.write(i[3])
                    file.close()
                    count += 1

    # reports number of files created. Not essential, but nice to know.
    # Creates or opens log file and prints this info to it
    log = open("log.txt", "a")

    print("Done! " + str(count) + " txt files created for patient " + patient + ".\n")
    log.write("Done! " + str(count) + " txt files created for patient " + patient + ".\n")
    if duplicates > 0:
        print("Deleted " + str(duplicates) + " duplicate txt files for patient " + patient + ".\n")
        log.write("Deleted " + str(duplicates) + " duplicate txt files for patient " + patient + ".\n")
    if skipped > 0:
        print("Skipped " + str(skipped) + " " + patient + " txt files due to error.\n")
        log.write("Skipped " + str(skipped) + " " + patient + " txt files due to error.\n")
    log.close()
    return directory


def getPatients(fileDir):
    """
    Gets all patients in a tab delimited file (assuming patients are included in the third column of said file)
    :param fileDir: The name of the TAB DELIMITED FILE (must be this format) to be read
    :return: Returns an array of all patient names found in file
    """
    # Creates array to store data
    data = []

    # open .tsv file
    with open(fileDir) as f:
        # Read data line by line
        for line in f:
            # split data by tab
            # store it in list
            listItem = line.split('\t')

            # append list to data
            data.append(listItem)
    # closes file
    f.close()

    # makes a new array to hold the names of each unique patient
    patients = []

    # reads through every entry in data and adds a name to the array if it isn't in there already
    for i in data:
        # Tries to ignore things that aren't names. Since the prompt had spaces, this was the quickest way to do that
        if " " in i[2]:
            continue
        found = False
        for j in patients:
            if i[2] == j:
                found = True
        if not found:
            patients.append(i[2])

    # Logs which patients are present and will be used, then returns the array
    log = open("log.txt", "a")
    log.write("Patients found: " + str(patients) + "\n")
    log.close()

    return patients
