**App Overview**

The application user interface was built with React Framework accompanied by a python framework flask and Scispacy for NLP on the back-end. This application allows users to identify medical terms in a note without programming or having to become a NLP expert. The application starts its work when the user uploads the excel and appropriate config file in json format to the upload sections. Flask then takes the excel file, converts it into dataframe and extracts certain sections to match criterias with the NLP config file. If certain keywords match with the extracted data frames then it passes 'Pass', for some matches it passes 'Review' and if the important terms are missing it passes 'Fail' to the flask as dataframe. Flask then sends the json response which is captured by React and is transformed into a table with student ID and other sections. Users can see the cases broadly by clicking on student ID. Results can be downloaded as an excel file for their local machine.

- **Usage Instruction**

**Data File Format**

- The file format has to be .xlsx
- The column names will be as follows - Timestamp( date as year month and day, time as hour minutes second, am or pm as in time region), Student\_ID(number as format), Case( has to be same as config file), Subjective(String), Objective(String), Assessment(String), Plan(String)

**Config File Format**

- The file format has to be json file
- For the writing format on json file, the case name will come first. Then we will have a subjective section. The Subject section will have three parts - Pass, fail and review.
- Pass, Fail, and Review will have these two terms for the identification of medical terms - name and cuis. We can also use certain terms for something specific naming as - term
- We will also have Objective, Assessment, and Plan section following the same terms or properties as Subjective.
- Each Case will have Subjective, Objective, Assessment, and Plan sections along with their own properties. An Example of this might be -

![Example image](https://github.com/VCU-CS-Capstone/CS-23-302-Software-platform-to-rate-clinical-notes-by-medical-students/blob/master/Documentation/ConfigFileExample.png)
