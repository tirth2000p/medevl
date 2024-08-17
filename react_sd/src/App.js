import React, {useState, useEffect} from 'react';
import './App.css';
import { Details,Menu,Navbar,Table} from './components'



function App(props) {
  const [showAnimated, setShowAnimated] = useState(() => {
    const storedValue = localStorage.getItem('showAnimated');
    return storedValue !== null ? JSON.parse(storedValue) : true;
  });

  // Sync the state with localStorage whenever it changes.
  useEffect(() => {
    localStorage.setItem('showAnimated', JSON.stringify(showAnimated));
  }, [showAnimated]);
  

  const [toggleMenu, setToggleMenu]= useState(() => {
    const storedValue = localStorage.getItem('toggleMenu');
    return storedValue !== null ? JSON.parse(storedValue) : false;
  });

  // Sync the state with localStorage whenever it changes.
  useEffect(() => {
    localStorage.setItem('toggleMenu', JSON.stringify(toggleMenu));
  }, [toggleMenu]);

  return (
    <div>
      <div className='container'>
      <div className='row no-gutters sticky-top'>
        <div className="col" >
          <Navbar toggleMenu={toggleMenu} setToggleMenu={setToggleMenu}/>
        </div>
      </div>
      <div className='row no-gutters'>

      {
        !showAnimated &&(
        <div className='col-sm-1'><Menu showAnimated={showAnimated} setShowAnimated={setShowAnimated}/>
        
        </div>
        
        )}
        {
        showAnimated &&(
          <>
        <div className='col-md-3'><Menu showAnimated={showAnimated} setShowAnimated={setShowAnimated}/></div>
        </>
        )}

<div className='col'><Table toggleMenu={toggleMenu} setToggleMenu={setToggleMenu} /></div>
      </div>
      </div>
      </div>
  );
}

export default App;