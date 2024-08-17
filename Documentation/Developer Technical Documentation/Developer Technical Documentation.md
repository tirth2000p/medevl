**Front End - React**

**Navbar Component:**

const [show, setShow] = useState(false);

` `const handleClose = () => setShow(false);

` `const handleShow = () => setShow(true);

This part is a react hook where using two props show and setShow to track the table component. handleClose and handleShow are two variables which will act upon the useState props when the detailed level cases are shown based on student ID. Users will be able to close that descriptive case where these variables are keeping track of user interaction. 

const state = {

`   `persons: []

` `};

Here the “state” variable explains an empty object which is created to catch or store data from the back-end.

function componentDidMount() {

`   `axios.get(`/sort`).then(res => {

`     `const persons = res.data;

`     `this.setState({ persons });

`   `});

` `}

The “componentDidMount” function is using axios to do a get request on file sort in the back-end to get data. We are storing that data to persons and using a react hook to confirm it.

On the return part of the Navbar component, bootstrap navbar style has been applied for different buttons such as Home, Info, Guide. Modal has been used from react-bootstrap on “info” button to customize the navbar button as a pop-up. 

**Menu Component:**

xport const Details = () => {

`   `const [showAnimated, setShowAnimated] = useState(false);

“Details” variable here is describing a react hook which has two props ‘showAnimated’ and ‘setShowAnimated’. The usual state is false here. This is used for the hamburger menu animation on the top of the front page beside the navbar.

`   `aria-label='Toggle navigation'

`             `onClick={() => setShowAnimated(!showAnimated)}



`           `>

`             `<div className={`animated-icon1 ${showAnimated && 'open'}`}>

`               `<span></span>

`               `<span></span>

`               `<span></span>

`             `</div>

`           `</MDBNavbarToggler>

`         `</MDBContainer>

`         `</MDBNavbar>

`       `<MDBCollapse show={showAnimated}>

In this area on return, we can see ‘onclick’ setShowAnimated has been reversed upon click on the hamburger menu where it will open the upload section where the user will upload their files. On the last last ‘MDBCollapse’ means clicking the menu again to collapse the whole upload section. 

**Table Component:**

useEffect(() => {

`     `fetchData()

` `},[] );

‘useEffect’ arrow has been created here to create an object ‘fetchData’ to fetch data from the back-end API. 

const fetchData = async () => {

` `const {data} = await axios.post('/uploader2')

` `setPosts(data)

}

‘fetchData’ object variable is getting data from ‘uploader2’ from the back-end. We are using Axios.post method here to interact with the API.

const Sort = async (by,asscending) => {

` `console.log(by,asscending)

axios.post('/sort',{column: by, order: asscending});

fetchData()

fetchData()

}

‘Sort’ variable here is used for showing the content of the table in ascending order. Again we are taking help of Axios.post method from the ‘sort’ file on the back-end to get the data.

const [data2, setData2] = useState('');

const [data3, setData3] = useState('');

const [data4, setData4] = useState('');

const [data5, setData5] = useState('');

const [data6, setData6] = useState('');

const [data7, setData7] = useState('');

const [data8, setData8] = useState('');

const [data9, setData9] = useState('');

const [data10, setData10] = useState('');

const [data11, setData11] = useState('');

const [data12, setData12] = useState('');

` `const parentToChild = (TimeStamp,note,Case,Flag,Reason,key,Comments,Subjective,Objective,Assessment,Plan) => {

`   `setData2(Case);

`   `setData3(TimeStamp);

`   `setData4(note);

`   `setData5(Flag);

`   `setData6(Reason);

`   `setData7(key);

`   `setData8(Comments);

`   `setData9(Subjective);

`   `setData10(Objective);

`   `setData11(Assessment);

`   `setData12(Plan);

` `}

Multiple react hooks have been created here to set different sets of data under a column name. As shown on the picture Case, flag, TimeStamp etc has been set apart from each other in to their different sections with variable names which comes altogether from the back-end.




**Details Component:**

const fetchData = async () => {

`   `const {data} = await axios.post('/uploader2')

`    `Table.setPosts(data)

` `}

‘fetchData’ arrow function here doing the same work as table component ‘fetchData’ fetching the data for the detailed description portion on details component.



const Final = async (key1,Final1) => {

`   `console.log(key1,Final1)

` `axios.post('/Final',{key: key1, Final: Final1});

`   `}

` `const Comment = async (key1,Comment1) => {

`   `console.log(key1,Comment1)

` `axios.post('/comment\_sent',{key: key1, comment: Comment1});

`  `}

`  `const Grade = async (key1,Flag1) => {

`   `console.log(key1,Flag1)

`  `axios.post('/Grade,{key: key1, Flag: Flag1});

`  `}

‘Final’ posts a value “done” as ‘Final1’ with auto-generated id as a key to flask route ‘/Final’.

‘Comment’ posts comment written by the user  as ‘Comment1’ with auto-generated id ‘key1’ as a key to flask route ‘/comment\_sent’.

‘Grade’ posts updated grade by user  as ‘Flag1’ with auto-generated id ‘key1’ as a key to flask route ‘/Grade’.

**Download Component:**

function Download(props){

const downloadExcel = (data) => {

`   `const worksheet = XLSX.utils.json\_to\_sheet(data);

`   `const workbook = XLSX.utils.book\_new();

`   `XLSX.utils.book\_append\_sheet(workbook, worksheet, "Sheet1");

`   `*//let buffer = XLSX.write(workbook, { bookType: "xlsx", type: "buffer" });*

`   `*//XLSX.write(workbook, { bookType: "xlsx", type: "binary" });*

`   `XLSX.writeFile(workbook, "GradeSheet.xlsx");

` `};

‘Download’ function here works as it is named, it is for downloading the data gotten back to the user. ‘downloadExcel’ arrow function is created to convert json data that’s been fetched from the back-end into .xlsx format for the user to download.












**Back-End -  Flask**

**App.py**

@app.route('/uploader', methods=['GET', 'POST'])

**def** uploader\_file():

`   `**if** request.method == 'POST':

`       `f = request.files['file']

`       `f.save(f.filename)

`       `print(f.filename)

`       `dataJSON = datasc.data\_ext(f.filename)

`       `# dataJSON = datasc.data\_ext('Clinical Skills Notes 2022 De-ID.xlsx')

`       `**with** open('data.json', 'w') **as** f:

`           `json.dump(dataJSON, f)

`       `**return** '', 204

‘uploader\_file’ function receives the file from a post request from the front-end and saves the file to the local directory. Then it passes the file to ‘datasc.py’ and receives the json data as ‘dataJSON’. It saves this json data as ‘data.json’ file and returns a 204 response.

@app.route('/uploader2', methods=['GET', 'POST'])

**def** uploaded\_file():

`   `f = open('data.json')

`   `dataJSON = json.load(f)

`   `response = app.response\_class(

`       `response=json.dumps(dataJSON),

`       `status=200,

`       `mimetype='application/json'

`   `)

`   `**return** response


‘uploaded\_file’ function creates a response using data from ‘data.json’ file with a status 200 and data type as ‘application/json’ and returns that response to get or post requests.

@app.route('/Grade', methods=['GET', 'POST'])

**def** edited():

`   `cm = request.json['Flag']

`   `key = request.json['key']

`   `dataJSON = change\_grade(key, cm)

`   `**with** open('data.json', 'w') **as** f:

`       `json.dump(dataJSON, f)

`   `**return** '', 204


‘edited’ function gets the key and flag from the json request  and passes them to the change\_grade function. The data received back from that function is stored in the data.json file. It returns a 204 response.

@app.route('/comment\_sent', methods=['GET', 'POST'])

**def** comment\_sent():

`   `cm = request.json['comment']

`   `key = request.json['key']

`   `dataJSON = comment\_add(key, cm)

`   `**with** open('data.json', 'w') **as** f:

`       `json.dump(dataJSON, f)

`   `**return** '', 204


‘comment\_sent’ function gets the key and flag from the json request  and passes them to the comment\_add function. The data received back from that function is stored in the data.json file. It returns a 204 response.

@app.route('/Final', methods=['GET', 'POST'])

**def** final():

`   `key = request.json['key']

`   `final1 = request.json['Final']

`   `print(key,final1)

`   `dataJSON = final\_check(key, final1)

`   `**with** open('data.json', 'w') **as** f:

`       `json.dump(dataJSON, f)

`   `**return** '', 204

‘final’ function gets the key and flag from the json request  and passes them to the final\_check function. The data received back from that function is stored in the data.json file. It returns a 204 response.



@app.route('/sort', methods=['GET', 'POST'])

**def** sort():

`   `order = request.json['order']

`   `column = request.json['column']

`   `dataJSON = sort\_input(order, column)

`   `**with** open('data.json', 'w') **as** f:

`       `json.dump(dataJSON, f)

`   `**return** '', 204

‘sort’ function gets the key and flag from the json request  and passes them to the sort\_input function. The data received back from that function is stored in the data.json file. It returns a 204 response.

**Sort.py**

**def sort\_input(order, column):**

`   `**# with open('data.json') as f:**

`   `**#     data1 = json.load(f)**

`   `**df = pd.read\_json('data.json')**

`   `**df = df.sort\_values(column, ascending=order)**

`   `**C1 = df[df.columns[0]].tolist()**

`   `**for i in range(len(C1)):**

`       `**C1[i] = i**

`   `**df['AutoID'] = C1**

`   `**thisisjson = df.to\_json(orient='records', date\_format='iso')**

`   `**parsed = json.loads(thisisjson)**

`   `**return parsed**

‘sort\_input’ function takes two attributes: order and column. It reads the data.json file using pandas and sort\_values with the attributes. It sets the ‘AutoID’ to column 1 on the list with variable C1 from the dataframe. ‘thisisjson’ variable orientates the records and sets the date.  It stores the data frame as json data, ‘parsed’ and returns ‘parsed’.


**Final.py**

**def** final\_check(key, fin):

`   `df = pd.read\_json('data.json')

`   `AutoID = df[df.columns[0]].tolist()

`   `Final = df[df.columns[4]].tolist()

`   `Final[int(key)] = fin

`   `df['Final'] = Final

`   `print(Final)

`   `thisisjson = df.to\_json(orient='records', date\_format='iso')

`   `parsed = json.loads(thisisjson)

`   `**return** parsed

‘final\_check’ function takes two attributes: key and fin. It reads the data.json file using pandas and converts it to dataframe. It takes the ‘AutoID’ and ‘Final’ columns from the dataframe. It updates new data with a new fin. It stores the data frame as json data, ‘parsed’ and returns ‘parsed’.





**changeGrade.py**

**def change\_grade(key, flg):**

`   `**df = pd.read\_json('data.json')**

`   `**AutoID = df[df.columns[0]].tolist()**

`   `**Flag = df[df.columns[5]].tolist()**

`   `**Flag[int(key)] = flg**

`   `**df['Flag'] = Flag**

`   `**thisisjson = df.to\_json(orient='records', date\_format='iso')**

`   `**parsed = json.loads(thisisjson)**

`   `**return parsed**

‘change\_grade’ function takes two attributes: key and flg. It reads the data.json file using pandas and converts it to dataframe. It takes the ‘AutoID’ and ‘Flag’ columns from the dataframe. It updates new data with a new ‘flg’. It stores the data frame as json data, ‘parsed’ and returns ‘parsed’.

**Comment.py** 

**def comment\_add(key, com):**

`   `**df = pd.read\_json('data.json')**

`   `**AutoID = df[df.columns[0]].tolist()**

`   `**Comments = df[df.columns[3]].tolist()**

`   `**Comments[int(key)] = com**

`   `**df['Comments'] = Comments**

`   `**thisisjson = df.to\_json(orient='records', date\_format='iso')**

`   `**parsed = json.loads(thisisjson)**

`   `**return parsed**


‘comment\_add’ function takes two attributes key and com. It reads the data.json file using pandas and convert it to dataframe. It takes the ‘AutoID’ and ‘Comments’ columns from the dataframe. It finds the particular comments using the key and updates it with new com. It stores the data frame as json data, ‘parsed’ and return ‘parsed’.






