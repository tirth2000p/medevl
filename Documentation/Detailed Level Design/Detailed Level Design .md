

**CS-23-302-Software platform to rate clinical notes by medical students**

**Detail Level Design**

**React Application for Front End (Interface Overview)**



`	`**Navbar Component:**

- Navbar components: different sections of the application that exist in a react component.
- Back: Come back to the previous page Home: Brings users back to the Home page.
- Info: holds the information about the product details such as application version.
- Guide: will guide the user how to use the application regarding table file format and config file format.
- The Info button is a pop up which will show information by clicking upon it.

`	`**Menu Component:**

- Menu Components: have two sections for uploading NLP as xlsx and Config file as txt.
- First Upload: uploads users xlsx and pass through NLP once it is submitted.
- Second Upload: uploads users config file as txt and pass.

`       `**Details Component:**

- Details page is about the clinical note document. 
- First: in the details page on the left side is Case which indicates case name.
- Second: Grade which indicates Pass or Fail. There is a button to edit the grade.Once clicked you can toggle between pass and fail and then you can click on the close button. 
- Third:Displays Full student notes about the patient. 
- Fourth: This section lists out reasons for the given grade. 
- Fifth: This section contains comments by the grading person. It could be edited by switching to edit mode and saved by closing out of edit mode.
- Final Button: clicking this button marts that particular entry as “done reviewing”.
- Sixth: This is the bottom most section, it displays the time stamp.

` 	`**Table Component:**

- Table page have 6 columns are 
- Student Id: when clicked toggle to details components view of that id. 
- Case: Displays the name of the case.
- Grade: Displays the pass or fail.
- Reasons: Displays the list of reasons for the given grade.
- Comments: Shows a comment mark if there is a comment made.
- Final Check: Shows a final check mark if final review is done. 
- Download button: Allows you to download the results as GradSheet xlsx file. 



**NLP:**

Using spaCy python library to perform

- Tokenization: separates blocks of text into separate strings
- POS Tagging: assigns a part of speech to each token
- Dependency Parsing: determines if certain tokens are linked by dependent phrasing
- Entity Recognition: links dependent phrases together into an entity

Using scispaCy python library to perform 

- Entity Linking, which allows us to recognize the CUIs or concept unique identifiers for each entity in the note. 

CUIs come from the UMLS (Unified Medical Language System) The note is then graded based on whether or not certain specific CUIs chosen by client are present or not.

Required CUIs are pulled from a file provided by the client, and the name of the file is passed in as an argument from the Flask application. A list of CUI’s is then pulled from the file, and then the extracted CUIs are compared to see if any match

Still needed:

- Abbreviation and Acronym expansion - expanding medical abbreviations and acronyms so that they are correctly recognized by spaCy
- Expanding case files - for the prototype, the algorithm only recognizes one case and one criteria, we need to expand it for all criteria.

**Flask:**

app.py:

A flask application to receive file uploaded by user to the backend server

`	`uploader\_file():

`		`If a file is sent to ‘/uploader’ using ‘POST’ method.

`		`It stores the requested file ‘f’.

It will save that file on the backend server with its original f.filename

It then passes that file to datasc.py for further processing of data and stores the data returned as dataJSON.

It stores the json data as data.json file so data can be returned to user when ever they want to access it until a new input file is provided.

It then ends with a 204 return.


uploaded\_file():

`	`If a ‘GET’ request is made to ‘/uploader2’.

`	`It loads the data.json file as a response

`	`And returns that response back to the ‘GET’ request.

datasc.py:

`	`On receiving xlsx or equivalent file from app.py it brakes that file into separate arrays in data frame ‘df’  for each column in that file using pandas read\_excel function.

`	`It then loops and passes each value in column 4 arrey(Notes) to the nlp module for further process.

`	`It receives result from nlp as tuple ‘tp’

`	`It adds 2 new columns and appends both value of tuple (Grade, Reason) to those columns for each data.

`	`It converts ‘df’ to json using to\_json and saves as ‘thisisjson’

`	`It performs json loads ‘thisisjson’ and saves as ‘parsed’

`	`It then returns ‘parsed’ to app.py



**



- ` `IPO Charts back end

|**Input**|**Process**|**Output**|
| :-: | :-: | :-: |
|` `**Student id**|||
|**Case Note**|` `Passes from react to flask , given to data scraper to break down the data one by one and pass it to NLP.| |
|**Config File**|` `NLP compares the data with config files and check if all requirements are met or not|Json Response|



- ` `IPO Charts React

|**Input**|**Process**|**Output**|
| :-: | :-: | :-: |
|` `**Student id**|||
|**Xlsx data sheet**|` `Passes From React to Flask |Displays data in table|
||` `Fetches data from flask using GET|Xlsx file|

` `IPO Chart NLP

|**Input**|**Process**|**Output**|
| :-: | :-: | :-: |
|**Text**|NLP to extract CUIs|CUIs present or missing|
|**Case** |Pull CUIs necessary for given case||
|||Xlsx |


