# uploader_file

* The uploader_file function is a POST request that takes in an excel file and returns the data as a JSON object.
    The function first saves the uploaded file to the server, then uses datasc.data_ext() to extract all of its data into
    a JSON object, which it then writes to 'data.json' on the server.

    :return: A 204 status code, which means that the request was processed successfully but there is no content to return
    :doc-author: Trelent

# config_file

* The config_file function is used to upload a configuration file to the server.
        The function takes in a POST request with the config file as an argument, and saves it on the server.

    :return: A 204 status code, which means that the request was successful but there is no content to return
    :doc-author: Trelent

# uploaded_file

* The uploaded_file function is a Flask route that returns the data.json file as a JSON object.

    :return: The json data from the file
    :doc-author: Trelent

# edited

* The edited function is called when the user clicks on the 'Edit' button.
    It takes in a key and a flag from the front end, which are used to find
    the correct student's grade in dataJSON. The function then changes that
    grade based on what was inputted by the user.

    :return: A 204 status code, which means that the request was successful but no content is returned
    :doc-author: Trelent

# comment_sent

* The comment_sent function is called when the user submits a comment.
    It takes in the comment and key from the request, adds it to dataJSON,
    and then writes that back to data.json.

    :return: A 204 status code, which means that the request was successful but there is no content to return
    :doc-author: Trelent

# final

* The final function is used to check the final answer of the user.
        It takes in a key and a Final value as input.
        The key is used to identify which question was answered by the user, and then it checks if that answer matches with our expected output or not.
        If it does match, then we return 204 status code (No Content) else we return 400 status code (Bad Request).

    :return: A 204 status code
    :doc-author: Trelent

# change_grade

* The change_grade function takes in a key and a grade. The key is the index of the student's record,
    and the grade is what we want to change it to. It then reads in data from our json file, and creates two lists:
    one for AutoID (the index) and one for Flag (the grades). We then change the value at that specific index
    to be equal to whatever new grade we want it changed to. Then we create a new column called 'Flag' which contains
    all of our updated grades, and return this as parsed json.

    :param key: Find the index of the record that is to be changed
    :param Grade: Change the grade of a student
    :return: A json file with the updated grade
    :doc-author: Trelent

# comment_add

* The comment_add function takes in a key and comment as parameters.
    The function then reads the data from the json file, creates lists of all columns,
    and adds the new comment to its corresponding key. The function then returns a parsed version of this updated json.

    :param key: Find the index of the row in which we want to add a comment
    :param com: Add a comment to the json file
    :return: The entire database with the new comment added
    :doc-author: Trelent

# data_ext

* The data_ext function takes in a filename and returns a JSON object.
    The function first checks the file extension of the inputted file, and if it is not an Excel (.xlsx) file, then it will return an error message.
    If the extension is correct, then it will read in all of the data from each column into lists (timestamp, studentID, case#...).
    It also creates empty lists for Flag (Pass/Fail), Reason (why Pass/Fail), Comments (user comments on why Pass/Fail), Final(Final decision by user).
    Then we loop through each row to check whether

    :param filename: Get the file extension and to read the data from that file
    :return: A json object
    :doc-author: Trelent

# final_check

* The final_check function takes in a key and a final value.
    The key is the index of the row that needs to be updated, and the final value is what will be placed into that row's Final column.
    This function returns an array of JSON objects with all rows from data.json.

    :param key: Find the index of the row that is being updated
    :param fin: Store the value of the final checkbox
    :return: A json file with the final check column updated to the value of fin
    :doc-author: Trelent

# set_case

* The set_case function takes two arguments:
    case - the name of the case to be used for testing.
    section - the section of that case to be tested.

:param case: Determine which case to use
:param section: Determine which section of the config
:return: A tuple of two lists
:doc-author: Trelent

# cui_search

* The cui_search function takes in a spaCy NLP document and a rule dictionary.
The function then searches the NLP document for entities that match the CUI(s)
specified in the rule dictionary. If an entity is found, it returns True and
the name of the term being searched for. If no entity is found, it returns False
and the name of the term being searched for.

:param nlp_doc: Pass the doc object from spacy to the function
:param rule: Pass in the rule that is being used to search for a term
:return: A list of two items
:doc-author: Trelent

# term_search

* The term_search function takes a text string, an nlp_doc object, and a rule dictionary as input.
It returns the term name (from the rule dictionary) if it finds any matches in the text string.
If no matches are found, it returns False.

:param text: Pass the text of a document to the function
:param nlp_doc: Create the matched_span object
:param rule: Pass the name and term of each rule to the function
:return: A list containing the following:
:doc-author: Trelent

# check

* The check function takes in a case, section, and text.
It then expands abbreviations in the text using abbreviation_expansion.
It sets the rules for that case and section using set_case.
The function then parses the text into tokens with nlp(text).
The pass conditions are initialized as an empty list to be filled later on.  The matched terms are also initialized as an empty list to be filled later on (this is used for highlighting).

:param case: Determine which rules to use
:param section: Determine which rules to use
:param text: Pass the text to be checked
:return: A tuple of (true/false, [list of missing terms], &quot;pass&quot;/&quot;review&quot;)
:doc-author: Trelent

# highlight_terms

* The highlight_terms function takes a spaCy Doc object and a list of matched terms,
and returns an HTML string with the matched terms highlighted.


:param doc: Pass in the document that we want to highlight
:param matched_terms: Pass in the list of matched terms
:return: An html string that can be rendered in a jupyter notebook
:doc-author: Trelent

# highlight_terms

* The abbreviation_expansion function takes a string as input and returns the same string with abbreviations expanded.
The function uses a JSON file to store the abbreviations and their expansions. The JSON file is read in, then each
abbreviation is searched for in the text using regex, and replaced with its expansion.

:param text: Pass in the text that will be searched for abbreviations
:return: The text with the abbreviations expanded
:doc-author: Trelent

# get_terms_and_cuis_from_config

* Myocardial infarction (MI), colloquially known as "heart attack,"
is caused by decreased or complete cessation of blood flow to a portion of the myocardium. 
Myocardial infarction may be "silent," and go undetected, or it could be a catastrophic event
leading to hemodynamic deterioration and sudden death. Most myocardial infarctions are due to 
underlying coronary artery disease, the leading cause of death in the United States. 
With coronary artery occlusion, the myocardium is deprived of oxygen. 
Prolonged deprivation of oxygen supply to the myocardium can lead to myocardial cell death and necrosis. 
Patients can present with chest discomfort or pressure that can radiate to the neck, 
jaw, shoulder, or arm. In addition to the history and physical exam, myocardial ischemia 
may be associated with ECG changes and elevated biochemical markers such as cardiac troponins. 
This activity describes the pathophysiology, evaluation, and management of myocardial infarction 
and highlights the role of the interprofessional team in improving care for affected patients. Hypertension

