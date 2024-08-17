import React, { useState } from 'react';
import {
  MDBContainer,
  MDBCollapse,
  MDBNavbar,
  MDBNavbarToggler,
} from 'mdb-react-ui-kit';
import './menu.css'

const Menu = (props) => {

  const handleSubmit = async (event, url) => {
    event.preventDefault();
    const formData = new FormData(event.target);

    const response = await fetch(url, {
      method: 'POST',
      body: formData,
    });

    if (response.status === 204) {
      window.location.reload();
    }
  };

  return (
    <>
      <MDBNavbar>
        <MDBContainer fluid>
          <MDBNavbarToggler
            type='button'
            className='first-button'
            data-target='#navbarToggleExternalContent'
            aria-controls='navbarToggleExternalContent'
            aria-expanded='false'
            aria-label='Toggle navigation'
            onClick={() => props.setShowAnimated(!props.showAnimated)}
          >
            <div className={`animated-icon1 ${props.showAnimated && 'open'}`}>
              <span></span>
              <span></span>
              <span></span>
            </div>
          </MDBNavbarToggler>
        </MDBContainer>
      </MDBNavbar>

      <MDBCollapse show={props.showAnimated}>
        <div className='bg-light shadow-3 p-4'>
          <p>Step 1:</p>
          <p>Upload Case Rules as a config.json file</p>
          <form onSubmit={(event) => handleSubmit(event, "http://127.0.0.1:5000/config")} enctype="multipart/form-data" >
            <div className="input-group mb-3">
              <input className="form-control" type="file" id="form-file" name="file"></input>
            </div>
            <div>
              <input className="submitbt btn btn-success" type="submit" ></input>
            </div>
          </form>
          <p>Step 2:</p>
          <p>Upload Student Notes</p>
          <p>Please attach only xlsx</p>
          <form onSubmit={(event) => handleSubmit(event, "http://127.0.0.1:5000/uploader")} enctype="multipart/form-data" >
            <div className="input-group mb-3">
              <input className="form-control" type="file" id="form-file" name="file"></input>
            </div>
            <div>
              <input className="submitbt btn btn-success" type="submit" ></input>
            </div>
          </form>
        </div>
      </MDBCollapse>
    </>
  );
}

export default Menu
