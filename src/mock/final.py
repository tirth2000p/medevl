import pandas as pd
import pathlib
import json

# need to change Final[int(key)], it changes with sort

def final_check(key, fin):
    """
    The final_check function takes in a key and a final value.
    The key is the index of the row that needs to be updated, and the final value is what will be placed into that row's Final column.
    This function returns an array of JSON objects with all rows from data.json.

    :param key: Find the index of the row that is being updated
    :param fin: Store the value of the final checkbox
    :return: A json file with the final check column updated to the value of fin
    :doc-author: Trelent
    """
    df = pd.read_json('data.json')

    AutoID = df[df.columns[0]].tolist()

    Final = df[df.columns[4]].tolist()

    Final[int(key)] = fin

    df['Final'] = Final
    print(Final)
    thisisjson = df.to_json(orient='records', date_format='iso')
    parsed = json.loads(thisisjson)

    return parsed


if __name__ == '__main__':
    final_check()
