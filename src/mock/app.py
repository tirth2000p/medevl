import os
from time import sleep

from flask import Flask, render_template, request, json
import datasc
from final import final_check
from comment import comment_add
from changeGrade import change_grade
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    """
    The uploader_file function is a POST request that takes in an excel file and returns the data as a JSON object.
    The function first saves the uploaded file to the server, then uses datasc.data_ext() to extract all of its data into
    a JSON object, which it then writes to 'data.json' on the server.

    :return: A 204 status code, which means that the request was processed successfully but there is no content to return
    :doc-author: Trelent
    """
    if request.method == 'POST':
        f = request.files['file']
        file_name = f.filename
        f.save(file_name)
        print(file_name)
        dataJSON = datasc.data_ext(file_name)
        with open('data.json', 'w') as json_file:
            json.dump(dataJSON, json_file)

        os.remove(file_name)
        return '', 204


@app.route('/config', methods=['GET', 'POST'])
def config_file():
    """
    The config_file function is used to upload a configuration file to the server.
        The function takes in a POST request with the config file as an argument, and saves it on the server.

    :return: A 204 status code, which means that the request was successful but there is no content to return
    :doc-author: Trelent
    """
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        print(f.filename)
        return '', 204

@app.route('/uploader2', methods=['GET', 'POST'])
def uploaded_file():
    """
    The uploaded_file function is a Flask route that returns the data.json file as a JSON object.

    :return: The json data from the file
    :doc-author: Trelent
    """
    f = open('data.json')
    dataJSON = json.load(f)
    response = app.response_class(
        response=json.dumps(dataJSON),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/Grade', methods=['GET', 'POST'])
def edited():
    """
    The edited function is called when the user clicks on the 'Edit' button.
    It takes in a key and a flag from the front end, which are used to find
    the correct student's grade in dataJSON. The function then changes that
    grade based on what was inputted by the user.

    :return: A 204 status code, which means that the request was successful but no content is returned
    :doc-author: Trelent
    """
    cm = request.json['Flag']
    key = request.json['key']
    dataJSON = change_grade(key, cm)
    with open('data.json', 'w') as f:
        json.dump(dataJSON, f)
    return '', 204

@app.route('/comment_sent', methods=['GET', 'POST'])
def comment_sent():
    """
    The comment_sent function is called when the user submits a comment.
    It takes in the comment and key from the request, adds it to dataJSON,
    and then writes that back to data.json.

    :return: A 204 status code, which means that the request was successful but there is no content to return
    :doc-author: Trelent
    """
    cm = request.json['comment']
    key = request.json['key']
    dataJSON = comment_add(key, cm)
    with open('data.json', 'w') as f:
        json.dump(dataJSON, f)
    return '', 204


@app.route('/Final', methods=['GET', 'POST'])
def final():

    """
    The final function is used to check the final answer of the user.
        It takes in a key and a Final value as input.
        The key is used to identify which question was answered by the user, and then it checks if that answer matches with our expected output or not.
        If it does match, then we return 204 status code (No Content) else we return 400 status code (Bad Request).

    :return: A 204 status code
    :doc-author: Trelent
    """
    key = request.json['key']
    final1 = request.json['Final']
    print(key,final1)
    dataJSON = final_check(key, final1)
    with open('data.json', 'w') as f:
        json.dump(dataJSON, f)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
