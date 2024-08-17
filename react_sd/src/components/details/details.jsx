import React, { useState, useEffect } from 'react'
import './details.css';
import Dropdown from 'react-bootstrap/Dropdown';
import axios from 'axios';
import Table from '../table/table';

function Details(props) {
  const [toggleEdit, setToggleEdit] = useState(true);
  const [toggleCommentEdit, setToggleCommentEdit] = useState(true);
  const [Flag, setFlag] = useState(props.Flag);
  const [comment, setComment] = useState(props.Comments);
  const [firstName, setFirstName] = useState(props.Comments);

  const fetchData = async () => {
    const { data } = await axios.post('/uploader2')

    Table.setPosts(data)
  }

  const Final = async (key1, Final1) => {
    console.log(key1, Final1)
    axios.post('/Final', { key: key1, Final: Final1 });

  }

  const Comment = async (key1, Comment1) => {
    console.log(key1, Comment1)
    await axios.post('/comment_sent', { key: key1, comment: Comment1 });
    setComment(Comment1);
  }

  const Grade = async (key1, Flag1) => {
    console.log(key1, Flag1)
    await axios.post('/Grade', { key: key1, Flag: Flag1 });
    setFlag(Flag1);
  }

  return (
    <div className="container de" id="details">
      <div className="row ">
        {/**Cases*/}
        <div className="col de-col col-md-8">
          <h4 id="Case" class="d-inline p-1 text-black"> Case: {props.Case}</h4>
        </div>

        {/**Grade: Edit and Save form */}
        {!toggleEdit && (
          <div className="col de-col col-md-3.5"><h4 id="Flag"> Grade: </h4>
            <Dropdown>
              <Dropdown.Toggle variant="success" id="Flag" >{props.Flag}
              </Dropdown.Toggle>
              <Dropdown.Menu>
                <Dropdown.Item value="Pass" onClick={e => Grade(props.Key, "Pass")}>Pass</Dropdown.Item>
                <Dropdown.Item value="Fail" onClick={e => Grade(props.Key, "Fail")}>Fail</Dropdown.Item>
                <Dropdown.Item value="Review" onClick={e => Grade(props.Key, "Review")}>Review</Dropdown.Item>
              </Dropdown.Menu>
            </Dropdown>
            <button className='btn btn-danger' onClick={() => setToggleEdit(true)} >Close</button>
          </div>
        )}

        {/*Grade view */}
        {toggleEdit && (<div className="col de-col col-md-3.5">
          <h4 id="Flag">
            Grade: {Flag} &nbsp;
            <button className='btn btn-warning' onClick={() => setToggleEdit(false)}>
              Edit
            </button>
          </h4>
        </div>
        )}
      </div>


      <div className="row row-2">
        {/**Notes*/}
        <div className="col de-col de-note col-lg-8"><h6 id="note">Note:</h6> <div dangerouslySetInnerHTML={{ __html: props.highlightedFullNote }}></div>
</div>
    {/**Reasons*/}
    <div className="col de-col col-md-3.5">
      <div className='row row-2'>
        <div className="col de-col de-reasons">
          <h6 id="Reason">Reasons: {props.reason}</h6>
        </div>
      </div>
      {/**Comment form- Edit and Save */}
      {!toggleCommentEdit && (
        <div className='row row-2'>
          <div className="col de-col de-comment">
            <h4 id="comment"> Comment:
              {/*Comment*/}
              <textarea className='Coment-text' value={firstName} name="Comment" onChange={e => setFirstName(e.target.value)} rows="7" />
            </h4>
            <button className='btn btn-warning' onClick={() => { Comment(props.Key, firstName); setToggleCommentEdit(true); }}>Close</button>
          </div>
        </div>
      )}

      {/*Comment view */}
      {toggleCommentEdit && (
        <div className='row row-2'>
          <div className="col de-col de-comment">
            <h4 id="comment"> Comment: </h4>
            <a></a> {comment} <a />
            <br></br>
            <br></br>
            <button className='btn btn-warning' onClick={() => setToggleCommentEdit(false)}>
              Edit
            </button>
            <br></br>
            <br></br>
          </div>
        </div>
      )}

    </div><div className='row'>
      {/*Final*/}
      <button className='btn btn3 btn-success' onClick={() => Final(props.Key, "Done")}>Final</button>
    </div>
  </div>

  {/**TimeStamp*/}
  <div className="row">
    <div className="col de-col"><h6 id="key">Time: {props.Timestamp}</h6></div>
  </div>

</div>
);
}

export default Details;
