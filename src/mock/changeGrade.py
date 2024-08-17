import pandas as pd
import pathlib
import json

# need to change Flag[int(key)], it changes with sort

def change_grade(key, Grade):

    """
    The change_grade function takes in a key and a grade. The key is the index of the student's record,
    and the grade is what we want to change it to. It then reads in data from our json file, and creates two lists:
    one for AutoID (the index) and one for Flag (the grades). We then change the value at that specific index
    to be equal to whatever new grade we want it changed to. Then we create a new column called 'Flag' which contains
    all of our updated grades, and return this as parsed json.

    :param key: Find the index of the record that is to be changed
    :param Grade: Change the grade of a student
    :return: A json file with the updated grade
    :doc-author: Trelent
    """
    df = pd.read_json('data.json')

    AutoID = df[df.columns[0]].tolist()

    Flag = df[df.columns[5]].tolist()

    Flag[int(key)] = Grade

    df['Flag'] = Flag

    thisisjson = df.to_json(orient='records', date_format='iso')
    parsed = json.loads(thisisjson)

    return parsed

if __name__ == '__main__':
    change_grade()

