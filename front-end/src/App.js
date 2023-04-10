import React, { useEffect, useState } from 'react';
import logo from './logo.png';
import './App.css';
import { Diagram } from './Diagram';
import { Total } from './Total';
import { Table } from './Table';


function App() {
  const [orders, setOrders] = useState([])

  function transformDate(data) {
    console.log(data)
    data.map(element => { 
      // Transform date to dd.mm.yyyy format
      const newDate = new Date(element.delivery_date)
      
      let day = newDate.getDate() 
      if (day < 10) day = '0' + day;
      
      let month = newDate.getMonth() + 1 
      if (month < 10) month = '0' + month;
      
      let year = newDate.getFullYear() 
      
      element.delivery_date = `${day}.${month}.${year}`
      
      return element
    });
  }

  useEffect(() =>{
    fetch("http://127.0.0.1:5000/", {
      method: "GET",
    })
    .then(response => response.json())
    .then(data => {setOrders(data.orders); console.log(data.orders); transformDate(data.orders)})
    .catch(e => console.log(e));
  },[])

  return (
    <div className="App">
      <div className='header'>
        <img src={logo} className="logo-pic" alt="logo" />
      </div>
      <div className='content'>
        <Diagram orders={orders}/>
        <div className='table-wrapper'>
          <Total orders={orders}/>
          <Table orders={orders}/>
        </div>
      </div>
    </div>
  );
}

export default App;
