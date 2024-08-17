import React, { useState } from 'react'
import './navbar.css';
import Modal from 'react-bootstrap/Modal';
import ListGroup from 'react-bootstrap/ListGroup';
import axios from 'axios';
import Dropdown from 'react-bootstrap/Dropdown';
import uparrow from '../../assets/Uparrow.png'
import Table from '../table/table';
import Download from '../download/download';

/**

* A component for displaying a navbar with a modal to submit a list of persons. It is used to provide a way to set properties on the component such as the number of people in the course of the app and the title of the app.
* 
* @param props - The props to display in the navbar.
* 
* @return { ReactElement } The component to display in the navbar as well as the modal to submit a list of persons

*/
function Navbar1 (props) {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const state = {
    persons: []
  };



    const handleClick = () => {
      props.setToggleMenu(false);
      window.location.reload();
    };
  
 
  return (
    <nav className="navbar navbar-custom justify-content-center">

  
     
        <button 
          className="btn btn-dark"
          type="submit"  
          onClick={handleClick}
        > Home
        </button>
  
      
     

      <button className="btn btn-dark"  type="button" onClick={handleShow}>Info</button>
        <Modal show={show} onHide={handleClose}   
        {...props}
        size="md"
        aria-labelledby="contained-modal-title-vcenter"
        centered>
          <Modal.Header closeButton>
            <Modal.Title>Application Information</Modal.Title>
          </Modal.Header>
              <Modal.Body>
                  <ListGroup variant="flush">
                      <ListGroup.Item>User Documentation: <a target="_blank" href='https://github.com/VCU-CS-Capstone/CS-23-302-Software-platform-to-rate-clinical-notes-by-medical-students/blob/master/Documentation/User%20Technical%20Document/User%20Technical%20Document.md'>User Technical Documentation</a> </ListGroup.Item>
                      <ListGroup.Item>Installation Documentation: <a target="_blank" href="https://github.com/VCU-CS-Capstone/CS-23-302-Software-platform-to-rate-clinical-notes-by-medical-students/blob/master/Documentation/Installation%20Doc-%20React%20App%20and%20NLP%20Sever/Installation%20Doc-%20React%20App%20and%20NLP%20Sever.md">Installation Guide</a></ListGroup.Item> 
                      <ListGroup.Item>Engineering  Documentation: <a target="_blank" href="https://github.com/VCU-CS-Capstone/CS-23-302-Software-platform-to-rate-clinical-notes-by-medical-students/blob/master/Documentation/Engineering%20Document/Engineering%20Document.md">Engineering Doc</a></ListGroup.Item>
                  </ListGroup>
              </Modal.Body>
        </Modal>
     
      {/* seperate here */}
      <form action="https://github.com/VCU-CS-Capstone/CS-23-302-Software-platform-to-rate-clinical-notes-by-medical-students/blob/master/Documentation/User%20Technical%20Document/User%20Technical%20Document.md" target="_blank">
         <button type="submit" className='btn btn-dark'>Guide</button>
      </form>


    <Download/>

    </nav>
  )
}

export default Navbar1
