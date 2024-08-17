import pandas as pd
import pathlib
import json
import scispacy_run

formats = ['.xlsx', '.xlsm', '.xlsb', '.xltx', '.xltm', '.xls', '.xlt', '.xls', '.xml', '.xml', '.xlam', '.xla', '.xlw',
           '.xlr']


def data_ext(filename):
    """
    The data_ext function takes in a filename and returns a JSON object.
    The function first checks the file extension of the inputted file, and if it is not an Excel (.xlsx) file, then it will return an error message.
    If the extension is correct, then it will read in all of the data from each column into lists (timestamp, studentID, case#...).
    It also creates empty lists for Flag (Pass/Fail), Reason (why Pass/Fail), Comments (user comments on why Pass/Fail), Final(Final decision by user).
    Then we loop through each row to check whether

    :param filename: Get the file extension and to read the data from that file
    :return: A json object
    :doc-author: Trelent
    """
    ext = pathlib.Path(filename).suffix
    if ext in formats:
        df = pd.read_excel(filename)

        autoID = []

        timestamp = df[df.columns[0]].tolist()

        studentID = df[df.columns[1]].tolist()

        case = df[df.columns[2]].tolist()

        Subjective = df[df.columns[3]].tolist()

        Objective = df[df.columns[4]].tolist()

        Assessment = df[df.columns[5]].tolist()

        Plan = df[df.columns[6]].tolist()

        #  FullNote = df[df.columns[7]].tolist()

        Flag = []

        Reasons = []

        Comments = []

        Final = []

        highlightedFullNote = []

        for i in range(len(Subjective)):
            autoID.append(i)
            Comments.append("")
            Final.append("")

            flagSub = scispacy_run.check(case[i], "subjective", Subjective[i])
            flagObj = scispacy_run.check(case[i], "objective", Objective[i])
            flagAss = scispacy_run.check(case[i], "assessment", Assessment[i])  # Fixed the typo in "Assesment"
            flagPlan = scispacy_run.check(case[i], "plan", Plan[i])

            if ("fail" in (flagSub[2].lower(), flagObj[2].lower(), flagAss[2].lower(), flagPlan[2].lower())):
                Flag.append("Fail")
            elif ("review" in (flagSub[2].lower(), flagObj[2].lower(), flagAss[2].lower(), flagPlan[2].lower())):
                Flag.append("Review")
            else:
                Flag.append("Pass")

            # temporarily checking just subjective.
            # Flag.append(flagSub[2])

            ## Need to provide reason from NLP ##
            # Reasons.append(flagSub[1])
            # highlightedFullNote.append(flagSub[3])

            Reasons.append("Subjective: " + str(flagSub[1]) + "\n Objective: " + str(flagObj[1]) + "\n Assesment: " + str(flagAss[1]) + "\n Plan: " + str(flagPlan[1]))
            highlightedFullNote.append("Subjective: " + str(flagSub[3]) + "\n Objective: " + str(flagObj[3]) + "\n Assesment: " + str(flagAss[3]) + "\n Plan: " + str(flagPlan[3]))


        df['Flag'] = Flag
        df['Reason'] = Reasons
        df['Comments'] = Comments
        df['Final'] = Final

        #df['FullNote'] = FullNote

        df['Subjective'] = Subjective
        df['Objective'] = Objective
        df['Assessment'] = Assessment
        df['Plan'] = Plan
        df['AutoID'] = autoID
        df['highlightedFullNote'] = highlightedFullNote
        print('PASS')

        thisisjson = df.to_json(orient='records', date_format='iso')
        parsed = json.loads(thisisjson)

        return parsed

if __name__ == '__main__':
    data_ext()

