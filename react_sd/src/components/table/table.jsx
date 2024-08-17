import React, {useState, useEffect} from 'react'
import './table.css';
import axios from "axios"
import Details from '../details/details';
import CloseButton from 'react-bootstrap/CloseButton';
import checkM from '../../assets/Eo_circle_green_checkmark.svg.png' 
import Download from '../download/download';
import BootstrapTable from 'react-bootstrap-table-next';
import paginationFactory from 'react-bootstrap-table2-paginator';
import filterFactory, { textFilter } from 'react-bootstrap-table2-filter';
import 'react-bootstrap-table-next/dist/react-bootstrap-table2.min.css';
import 'react-bootstrap-table2-paginator/dist/react-bootstrap-table2-paginator.min.css';

// Creates a table that can be used to toggle the status of students. 

const Table = ({ toggleMenu, setToggleMenu }) => {

  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  // This is called when we have a response. It's the responsibility of the caller to ensure that the response is indeed valid
  useEffect(() => {
    setLoading(true);
    axios.get('/uploader2')
      .then(response => {
        setData(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error(error);
        setLoading(false);
      });
  }, []);


  // Outputs data for a single student. TODO ( johannesburg ) : This is a copy of the logic in service. js
  const columns = [
    {
      dataField: 'Student_ID',
      text: 'Student_ID',
      sort: true,
      filter: textFilter(),
      formatter: (cell, row)=> <a href={`/details/${row.Student_ID}`}>{row.Student_ID}</a>
    },
    {
      dataField: 'Case',
      text: 'Case',
      sort: true,
      filter: textFilter()
    },
    {
      dataField: 'Flag',
      text: 'Grade',
      sort: true,
      filter: textFilter()
    },
    {
      dataField: 'Reason',
      text: 'Reason',
      sort: true,
      filter: textFilter()
    },
    {
      dataField: 'Comments',
      text: 'Comments',
      
    },
    {
        dataField: 'Final',
        text: 'Final Check',
        sort: true,
        
    },
    
  ];

  // Creates a config object that will be used to configure the service. By default this config is 10
  const options = {
    sizePerPage: 12,
    hideSizePerPage: true,
    hidePageListOnlyOnePage: true,
  };




//  const [data2, setData2] = useState('');
// const [data3, setData3] = useState('');
// const [data4, setData4] = useState('');
// const [data5, setData5] = useState('');
// const [data6, setData6] = useState('');
// const [data7, setData7] = useState('');
// const [data8, setData8] = useState('');
// const [data9, setData9] = useState('');
// const [data10, setData10] = useState('');
// const [data11, setData11] = useState('');
// const [data12, setData12] = useState('');

  // const parentToChild = (TimeStamp,note,Case,Flag,Reason,key,Comments,Subjective,Objective,Assessment,Plan) => {
  //   setData2(Case);
  //   setData3(TimeStamp);
  //   setData4(note);
  //   setData5(Flag);
  //   setData6(Reason);
  //   setData7(key);
  //   setData8(Comments);
  //   setData9(Subjective);
  //   setData10(Objective);
  //   setData11(Assessment);
  //   setData12(Plan);
  // }

  // This is how to use localStorage. setItem ('detailsProps')
  const [detailsProps, setDetailsProps] = useState(() => {
    const storedProps = localStorage.getItem('detailsProps');
    return storedProps !== null
      ? JSON.parse(storedProps)
      : {
          Case: '',
          Key: '',
          // Add all other props with their default values.
          note: '',
          Flag: '',
          reason: '',
          Timestamp: '',
          Comments: '',
          Subjective: '',
          Objective: '',
          Assessment: '',
          Plan: '',
          highlightedFullNote: '',
        };
  });

  // Sync the state with localStorage whenever it changes.
  useEffect(() => {
    localStorage.setItem('detailsProps', JSON.stringify(detailsProps));
  }, [detailsProps]);

  // ... other constants and functions

  const parentToChild = (
    TimeStamp,
    note,
    Case,
    Flag,
    Reason,
    key,
    Comments,
    Subjective,
    Objective,
    Assessment,
    Plan,
    highlightedFullNote
  ) => {
    setDetailsProps({
      Case,
      Key: key,
      note,
      Flag,
      reason: Reason,
      Timestamp: TimeStamp,
      Comments,
      Subjective,
      Objective,
      Assessment,
      Plan,
      highlightedFullNote,
    });
  };

  



  return (
   
      <div className="container" >
        {/* <Download data={}/> */}
        {
        !toggleMenu &&(
          <div>
          {loading ? (
            <p>Loading...</p>
          ) : (
            
            <BootstrapTable 
              bootstrap4
              striped  
              bordered
              keyField='id' 
              data={data} 
              columns={[
                {
                  dataField: 'Student_ID',
                  text: 'Student ID',
                  sort: true,
                  filter: textFilter(),
                  formatter: (cell, row) => <a href={`#details`} onClick={()=> {parentToChild(row.Timestamp,row.FullNote,row.Case,row.Flag,row.Reason,row.AutoID,row.Comments,
                    row.Subjective,row.Objective,row.Assessment,row.Plan,row.highlightedFullNote);setToggleMenu(true);}}>{row.Student_ID}</a>,
                  headerStyle: {
                    backgroundColor: '#F8B300',  
                    color: '#000000',
                    fontWeight: 'bold',
                    fontSize: '16px',
                    textAlign: 'center',
                  },
                },
                {
                  dataField: 'Case',
                  text: 'Case',
                  sort: true,
                  filter: textFilter(),
                  headerStyle: {
                    backgroundColor: '#F8B300',
                    color: '#000000',
                    fontWeight: 'bold',
                    fontSize: '16px',
                    textAlign: 'center',
                  },
                },
                {
                  dataField: 'Flag',
                  text: 'Grade',
                  sort: true,
                  filter: textFilter(),
                  headerStyle: {
                    backgroundColor: '#F8B300',
                    color: '#000000',
                    fontWeight: 'bold',
                    fontSize: '16px',
                    textAlign: 'center',
                  },
                },
                {
                  dataField: 'Reason',
                  text: 'Reason',
                  sort: true,
                  headerStyle: {
                    backgroundColor: '#F8B300',
                    color: '#000000',
                    fontWeight: 'bold',
                    fontSize: '16px',
                    textAlign: 'center',
                  },
                },
                {
                  dataField: 'Comments',
                  text: 'Comments',
                  sort: true,
                  formatter: (cell,row) =>{
                    if(cell){
                      const words = cell.split(' ');
                      const firstWords = words.slice(0,3).join(' ');
                      return firstWords+" ...";
                   }
                    
                  },
                  headerStyle: {
                    backgroundColor: '#F8B300',
                    color: '#000000',
                    fontWeight: 'bold',
                    fontSize: '16px',
                    textAlign: 'center',
                  },
                },
                {
                  dataField: 'Final',
                  text: 'Final Check',
                  sort: true,
                  formatter: (cell, row) =>{
                    if (cell) {
                      return (<img className="img" src={checkM}/> )
                    }
                    else {
                      return "";
                    }
                  },
                  headerStyle: {
                    backgroundColor: '#F8B300',
                    color: '#000000',
                    fontWeight: 'bold',
                    fontSize: '16px',
                    textAlign: 'center',
                    
                  },
                },
              ]}
              // rowStyle={(row, rowIndex) => ({
              //   backgroundColor: rowIndex % 2 === 0 ? '#FFFFFF' : '#E5CBB1',
              //   '&:hover': {
              //     backgroundColor: 'blue',
              //     color: 'white',
              //   },
              // })}
              pagination={paginationFactory(options)}
              filter={filterFactory()}
            />
          )}
          
          </div>
          )}
          {
        toggleMenu &&(
          <div className='row no-gutters'>
            <div className="container de" >
  <div className='col'>
  <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
    <CloseButton  className='bg-danger shadow-1-strong' size="lg" onClick={() => { setToggleMenu(false); window.location.reload(); }} href='#table'  />
    </div>
  <Details      Case={detailsProps.Case}
                Key={detailsProps.Key}
                note={detailsProps.note}
                Flag={detailsProps.Flag}
                reason={detailsProps.reason}
                Timestamp={detailsProps.Timestamp}
                Comments={detailsProps.Comments}
                Subjective={detailsProps.Subjective}
                Objective={detailsProps.Objective}
                Assessment={detailsProps.Assessment}
                Plan={detailsProps.Plan} 
                highlightedFullNote={detailsProps.highlightedFullNote}/>
  </div>
  </div>
  </div>)}
  
      </div>

  )
}

export default Table