import pandas as pd
import pathlib
import json

# need to change Comments[int(key)], it changes with sort

def comment_add(key, com):
    """
    The comment_add function takes in a key and comment as parameters.
    The function then reads the data from the json file, creates lists of all columns,
    and adds the new comment to its corresponding key. The function then returns a parsed version of this updated json.

    :param key: Find the index of the row in which we want to add a comment
    :param com: Add a comment to the json file
    :return: The entire database with the new comment added
    :doc-author: Trelent
    """
    df = pd.read_json('data.json')

    AutoID = df[df.columns[0]].tolist()

    Comments = df[df.columns[3]].tolist()

    Comments[int(key)] = com

    df['Comments'] = Comments

    thisisjson = df.to_json(orient='records', date_format='iso')
    parsed = json.loads(thisisjson)

    return parsed

if __name__ == '__main__':
    comment_add()

