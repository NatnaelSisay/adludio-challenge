import './App.css';
import React, { useEffect } from 'react';
import { useState } from 'react';
import axios from 'axios';

// Fetch data from server and setup on the drow down
// send a request and check the result

function App() {
  const [codes, setSoces] = useState()
  useEffect(() => {
      axios.get('http://127.0.0.1:5000/').then(res => {
        
        // console.log(res.data['CampainId'])
        let result = res.data['CampainId']
        setSoces(result)
      })
  },[])

  console.log(codes)
  return (
    <div className="App">
      <ul>
      {  codes?.map((element, index) => {
        return <li key={index}>{element}</li>
      }) }
      </ul>
      
    </div>
  );
}

export default App;
