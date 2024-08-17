import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import ListGroup from 'react-bootstrap/ListGroup';
import Popup from 'reactjs-popup';
import { render } from '@testing-library/react';

function Info (props) {
  const [show, setShow] = useState(false);
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
   
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
                  <ListGroup.Item> Documentation: Clincial Notes User Manual</ListGroup.Item>
                  <ListGroup.Item>Tutorials: How to Upload</ListGroup.Item>
              </ListGroup>
          </Modal.Body>
    </Modal>
  );
  }
export default Info;