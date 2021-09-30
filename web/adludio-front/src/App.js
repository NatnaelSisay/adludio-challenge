import './App.css'
import React, { useEffect, useState } from 'react'

import axios from 'axios'

function App () {
  const [codes, setSoces] = useState()
  const [selectedCode, setSelectedCode] = useState('')
  const [filterResult, setFilterResult] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/').then(res => {
      // console.log(res.data['CampainId'])
      const result = res.data.CampainId
      setSoces(result)
    })
  }, [])

  const getListing = () => {
    if (!selectedCode | selectedCode === 'default') { return }

    axios.get(`http://127.0.0.1:5000/${selectedCode}`)
      .then(res => {
        const data = res.data[selectedCode]
        setFilterResult(data)
        console.log(data)
      })
  }

  const handleSelectChange = (e) => {
    setSelectedCode(e.target.value)
  }

  console.log('selected code ', selectedCode)
  return (
    <div className='App'>

      <select value={selectedCode} onChange={(e) => handleSelectChange(e)}>
        <option key='default' value='default'>Choose Code </option>
        {
              codes?.map(code => {
                return <option key={code}>{code}</option>
              })
        }
      </select>

      <button onClick={() => getListing()}>Get Top Sites</button>

      {
        filterResult.length
          ? <div>
            <h2>Total Result {filterResult.length}</h2>
            <ul className='table-view'>
              {
                      filterResult?.map((element, index) => {
                        return (
                          <li key={index}>{element} </li>
                        )
                      })
                    }
            </ul>
          </div>

          : ''
      }

    </div>
  )
}

export default App
