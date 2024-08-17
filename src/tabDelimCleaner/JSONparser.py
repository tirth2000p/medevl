import csv
import json
import os
import pandas as pd
from ast import literal_eval
import re
from csv import writer


def reader(fileDir):
    """
    Converts a JSON file to a dictionary and CSV file, returns directory of the graded file folder.
    Only tested with WSD + JSON format. Use caution if this isn't your use case.
    :param fileDir: The directory with all JSON files to be read
    :return: Directory of folder that holds outputted CSV files
    """
    log = open("log.txt", "a")
    # makes a list of all files in the given folder
    files = os.listdir(fileDir)
    # Makes a folder
    gradedFiles = fileDir + "/GradedFiles"
    if not os.path.isdir(gradedFiles):
        os.mkdir(gradedFiles)
    # Opens each file in the directory and extracts the cuis
    for i in files:
        # Prevents the folder already existing from causing an error
        if i == "gradedFiles":
            continue

        # Makes sure metamap didn't pass an empty file. This happens sometimes.
        # Try to restart your computer before running metamap to mitigate empty or truncated file returns.
        if os.path.getsize(fileDir + "/" + i) == 0:
            print(i + " is empty; this is a metamap error. Manual grading required for this file.")
            log.write(i + " is empty; this is a metamap error. Manual grading required for this file.\n")
            continue
        f = open(fileDir + "/" + i)

        # This try/catch determines if metamap abruptly stopped writing to the JSON file, which tends to give json.load
        # a seizure.
        try:
            # Makes a string with json file data, easier for me to remove sections while this is a string
            # I'm removing sections because I removed some when figuring this out.
            # I couldn't figure out how to make it work with full structure.
            current = str(json.load(f))
            f.close()
        except(Exception):
            print(i + " is incomplete, this is a metamap error. Manual grading required for this file.")
            log.write(i + " is incomplete, this is a metamap error. Manual grading required for this file.\n")
            continue

        # This one should only error out if there's a formatting issue
        try:
            # Finds the closest comma from 'AAs', cuts at that comma, adds { in front, removes now-unnecessary wrapping
            current = "{" + current[current.find(",", current.find('AAs')) + 2: len(current) - 3]
            current = literal_eval(current)
            # Holds all data
            dataHolder = {}
            dataArray = []
            # Enters the dictionary
            for j in current:
                # Gives me utterances, different processes for each b/c structure differences
                if j == "Utterances":
                    # Big dictionary subdivision for my sanity.
                    bigList = {}
                    bigList["Lines"] = []
                    # Enters an utterance
                    for pos in current[j]:
                        # Creates an empty list to hold all info
                        listAppend = {}
                        # Gets the line
                        listAppend["Line"] = pos["UttText"]
                        listAppend["PhraseInfo"] = []
                        # Enters the phrase section (metamap's line by line analysis results)
                        for phrase in pos["Phrases"]:
                            # I'm going to hate myself soon, but makes a dict to hold phrase information
                            phraseInList = {}
                            phraseInList["Phrase"] = phrase["PhraseText"]
                            phraseInList["StartPosition"] = phrase["PhraseStartPos"]
                            phraseInList["MappingInfo"] = []
                            for mapped in phrase["Mappings"]:
                                # I'm going to hate myself even more, but this holds mapping information for each phrase
                                mappings = {}
                                mappings["MappingScore"] = mapped["MappingScore"]
                                mappings["CandidateInfo"] = []
                                for candidate in mapped["MappingCandidates"]:
                                    # Why. Candidate information for each mapping for each phrase for each positive utterance
                                    candInfo = {}
                                    candInfo["CuiScore"] = candidate["CandidateScore"]
                                    candInfo["Cui"] = candidate["CandidateCUI"]
                                    candInfo["CandidateMatched"] = candidate["CandidateMatched"]
                                    candInfo["CandidatePreferred"] = candidate["CandidatePreferred"]
                                    # Makes array to hold data, also hijacks the decision structure to make "Negated" in dictionary
                                    if candidate["Negated"] == "1":
                                        dataArray.append([candidate["CandidateCUI"], candidate["CandidateMatched"],
                                                          candidate["CandidatePreferred"],
                                                          candidate["CandidateScore"],
                                                          mapped["MappingScore"], phrase["PhraseText"],
                                                          phrase["PhraseStartPos"], True, pos["UttText"]])
                                        candInfo["Negated"] = True
                                    else:
                                        dataArray.append([candidate["CandidateCUI"], candidate["CandidateMatched"],
                                                          candidate["CandidatePreferred"],
                                                          candidate["CandidateScore"],
                                                          mapped["MappingScore"], phrase["PhraseText"],
                                                          phrase["PhraseStartPos"], False, pos["UttText"]])
                                        candInfo["Negated"] = False
                                        # It's the end of the nest. Appends candInfo to mappings, and etc.
                                    mappings["CandidateInfo"].append(candInfo)
                                if mappings: phraseInList["MappingInfo"].append(mappings)
                            if phraseInList["MappingInfo"]: listAppend["PhraseInfo"].append(phraseInList)
                        bigList["Lines"].append(listAppend)
                    dataHolder["Data"] = bigList
        # This is the only reason I can think of for this to fail. Either my structure is wrong, or theirs is.
        except(Exception):
            print("Error reformatting " + i + ". This is either a metamap output error or a programmatic oversight. Manual grading required for this file.")
            log.write("Error reformatting " + i + ". This is either a metamap output error or a programmatic oversight. Manual grading required for this file.\n")
            continue

        # This is in a try/catch for if you forgot to delete the graded files created the last time you ran this.
        # Make sure to do that.
        try:
            # turns the 2d array into a dataframe and prints it to csv
            df = pd.DataFrame(dataArray,
                              columns=["Cui", "CandidateMatched", "CandidatePreferred", "CuiScore", "MappingScore",
                                       "Phrase", "StartPosition", "IsPositive", "Line"])
            df.to_csv(gradedFiles + "/" + i[0: len(i) - 5] + ".csv", index=False)
        # Error message in case metamap truncates file.
        except(Exception):
            print(i + " already exists; this is a user/filesystem error. Manual grading required for this file.")
            log.write(i + " already exists; this is a user/filesystem error. Manual grading required for this file.\n")
            continue
    log.close()
    return gradedFiles


def grader(fileDir, configDir, maxScore):
    '''
    Grades all files in a given folder based on the instructions written in a given config file.
    The actual grading logic for this one is kind of messy, and for that I deeply apologise

    :param fileDir: Points to the directory of the input/output folder.
    :param configDir: Points to the config file.
    :param maxScore: Allows user to define number of points total for grading.
    :return: Nothing, as of right now.
    '''
    # Opens error log file
    log = open("log.txt", "a")
    # makes a list of all files in the given folder
    files = os.listdir(fileDir)
    for i in files:
        score = maxScore
        # Creates an array of CUIs found in the current CSV file
        cuiArray = []
        with open(fileDir + "/" + i) as x:
            for line in x:
                # split data by comma, store it in list
                inLine = line.split(",")
                cuiArray.append(inLine)
            x.close()

        # opens the config file and extracts the cui list
        # The last comma delimited entry must be empty, this allows me to delete the newline in the list
        # Like this, the format created should be:
        # first layer- lines, second layer- tags + comma seperated values, third layer- alternates

        # Tags should be put in front of each line to determine that line's rules:
        # For instance, e- is an elimination line, pass/fail. They should be at the top, but don't have to be.
        # Integers, such as 10- , 15- , or 50- , determine how many points each item on the line is worth.
        # If an int item is not found, then that int is subtracted from the final score
        # Other tags can be created and added if wanted, implementing them would be pretty easy

        guideCuis = []
        with open(configDir) as c:
            # Read data line by line
            for line in c:
                # skips lines if commented out by "#" or if empty
                if line[0:1] != "#" and len(line) > 0 and line != "\n":
                    # Gets the tag and removes it from the line
                    lineList = [line[0:line.find("-")]]
                    line = line[line.find(" ") + 1: len(line)]
                    # split data by comma, store it in list
                    lineList += line.split(",")
                    # separates the colon delimited values and places them in a list, if they exist
                    l = 1
                    while l < len(lineList):
                        if lineList[l].find(":") > 0:
                            lineList[l] = (lineList[l]).split(":")
                        l += 1
                    # Removes the newline character because it's annoying
                    del lineList[len(lineList) - 1]
                    guideCuis.append(lineList)
        # closes file
        c.close()
        # Creates a file to store results
        # (You may be going through this program right now and going "Wow, why is this person using the x flag all the
        # time when making files, it throws errors like crazy." I want it to throw errors. It only errors out in testing
        # scenarios, which aren't really a real use case. If it EVER errors out in a non-testing scenario, I either have
        # it in a try catch that deals with the error, or it's in a place where there REALLY shouldn't be an error.)
        grad = open(fileDir + "/" + i[0: len(i) - 4] + ".grad", "x")
        # Opens the table results file and the writer for it as well. If it doesn't exist, makes the headers as well.
        exists = False
        if os.path.isfile('tableResults.csv'):
            exists = True
        result = open('tableResults.csv', 'a', newline='')
        writer = csv.writer(result)
        if not exists:
            writer.writerow(["Patient", "Student Id", "Pass/Fail", "Score (If Applicable)"])

        # sees if config file's cuis are present in document
        # enters each line in config cui list
        failure = False
        for line in guideCuis:
            failure = False
            # Sees if there's any overlap with the items in the line
            for item in line:
                # Makes sure it isn't processing a tag by mistake
                if not (type(item) is str and len(item) < 3):
                    found = False
                    timesFound = 0
                    header = False
                    for cui in cuiArray:
                        # Sees if there's or structure, and if there is, makes sure that the or structure isn't a header
                        if type(item) is list:
                            for altObject in item:
                                # Does regex to see if it's actually a CUI
                                match = re.fullmatch("C\d{7}", altObject)
                                # If it's not a CUI
                                if match is None:
                                    header = True
                                elif altObject == cui[0]:
                                    found = True
                                    timesFound += 1
                        elif item == cui[0]:
                            found = True
                            timesFound += 1
                    # Prints if the item was found or not found
                    if header == True:
                        theItem = str(item[0])
                    else:
                        theItem = str(item)
                    if not found:
                        # Tries to dock points, if this doesn't work then I guess it was passed a letter flag.
                        # If it's passed an invalid flag it will also error out, but then it would just get skipped.
                        try:
                            score -= int(line[0])
                            grad.write("Score -" + line[0] + " points: " + theItem + " absent.   ")
                        except:
                            if line[0] == "e":
                                grad.write("Failure: required cui " + theItem + " absent.   ")
                                failure = True
                            # You can put elifs here for more tags
                            # Prints tag failures and records the occurrence to log
                            else:
                                print("Invalid grading tag passed. Line contianing " + str(line) + " skipped.")
                                log.write("Invalid grading tag passed. Line contianing " + str(line) + " skipped.\n")
                    else:
                        if line[0] == "e":
                            grad.write(theItem + ", present (found  " + str(timesFound) + " times.)   ")
                        # You can put elifs here for more tags
                        else:
                            grad.write(theItem + ", present (found  " + str(timesFound) + " times.)   ")
            grad.write("\n")
            # If this is an e line and a term wasn't found, writes the failure to result and goes to next file.
            if line[0] == "e" and failure:
                writer.writerow([i[i.find("_") + 1: len(i) - 4], i[0: i.find("_")], "Failure", None])
                break
        # Prints score if it didn't fail. Extra new line to make the score stand out a bit more
        if not failure:
            grad.write("\nFinal score: " + str(score))
            writer.writerow([i[i.find("_") + 1: len(i) - 4], i[0: i.find("_")], "Pass", str(score)])
        log.close()
        grad.close()
        result.close()

grader("/home/em-is-an-em/PycharmProjects/tabDelimCleaner/PatientData/CageData/metamapOutput (WSD + JSON)/GradedFiles", "/home/em-is-an-em/PycharmProjects/tabDelimCleaner/CompareAgainst.txt", 100)
