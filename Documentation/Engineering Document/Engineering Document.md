**Business Requirements**

- Accepts excel file upload with format .xlsx, .xls, .xlsm, .xlsb, .xlam
- Given a set of clinical concepts, uses NLP to determine whether each concept is present in each note
- Given a set of criteria, assign each note a grade of "Pass", "Fail", or “Review”
- Users can review the concepts detected in each note with corresponding text highlights
- Users can review the grade for each note and add their comments to it
- Users can download results with .xlsx format

**Functional and Non-functional Requirements**

- React framework along with bootstrap, CSS, HTML to accomplish the High Level Design and Interface for the user experience.
- Flask framework to receive and scratch data to NLP for evaluation and sending the result back to the frontend application.
- NLP framework to evaluate the data for grade and forward it to flask framework.

**Technical Requirements**

- UMLS and scispacy as the NLP framework 
- Format of the data that to pass towards front-end from flask

**Prioritization**

- Business requirements must be met to make the user experience clear and concise. Reviewing each notes with comments must be achieved
- Functional dependencies must be operable to make the whole application working. Non functional dependencies yet to decide
- Either UMLS or scispacy is needed for the NLP framework to determine the grade along with the data type to get back to the front-end.
