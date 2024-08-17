import * as XLSX from 'xlsx';
import downIC from '../../assets/Download-Icon.png'
import './download.css'
import * as FileSaver from 'file-saver';
import axios from "axios"

function Download(){

  const fileType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8';
  const fileExtension = '.xlsx';



  const exportToCSV = async () => {
    const { data } = await axios.get('/uploader2');
    const dataToExport = data.map((item) => ({
      Student_ID: item.Student_ID,
      Case: item.Case,
      Flag: item.Flag,
      Subjective: item.Subjective,
      Objective: item.Objective,
      Assessment: item.Assessment,
      Plan: item.Plan,
      Reason: item.Reason,
      Comments: item.Comments,
      Final: item.Final,
      FullNote: item.FullNote,
      Timestamp: item.Timestamp,
      highlightedFullNote: item.highlightedFullNote,
    }));

    const ws = XLSX.utils.json_to_sheet(dataToExport);
    const wb = { Sheets: { data: ws }, SheetNames: ['data'] };
    const excelBuffer = XLSX.write(wb, { bookType: 'xlsx', type: 'array' });
    const dataBuffer = new Blob([excelBuffer], { type: fileType });
    FileSaver.saveAs(dataBuffer, 'data' + fileExtension);
  };

  return(
    <button className='btn btn2 btn-dark position-absolute top-0 end-0' onClick={exportToCSV}>
<img className='img2' src={downIC} />
</button>
)
  }
export default Download;