import './App.css'
import React, { useEffect, useState } from 'react'

import axios from 'axios'

const BASE_URL = 'http://127.0.0.1:5000'
const DEFAULT = 'default'

function App () {
  const [campainIds, setCampainIds] = useState()
  const [selectedCampainId, setSelectedCampainId] = useState('')
  const [filterResult, setFilterResult] = useState([])

  // ---- CUSTOM FUNCTIONS ---- //
  const fetchSitesOfSelectedCampain = () => {
    if (!selectedCampainId | selectedCampainId === DEFAULT) { return }

    axios.get(`${BASE_URL}/${selectedCampainId}`)
      .then(res => {
        const data = res.data[selectedCampainId]
        setFilterResult(data)
      })
  }

  // ---- CUSTOM FUNCTIONS ---- //

  useEffect(() => {
    axios.get(BASE_URL).then(res => {
      const result = res.data.CampainId
      setCampainIds(result)
    })
  }, [])

  return (
    <div className='layout-container'>

      <div className='container'>

        <aside>
          <select
            value={selectedCampainId}
            onChange={(e) => setSelectedCampainId(e.target.value)}
            className='select-options'
          >
            <option key={DEFAULT} value={DEFAULT}>Campain Id's </option>
            {
                campainIds?.map(code => {
                  return <option key={code}>{code}</option>
                })
          }
          </select>

          <button
            onClick={() => fetchSitesOfSelectedCampain()}
            className='aside-button'
          >Get Top Sites
          </button>
        </aside>

        <main>

          {
        filterResult.length
          ? <div>
            <h2>Total Result <span className='badge'>{filterResult.length}</span> </h2>
            <ul className='table-view'>
              {
                      filterResult?.map((element, index) => {
                        return (
                          <li key={index}>
                            <a
                              rel='external'
                              className='fab fa-instagram'
                              href={`http://${element}`}
                            >
                              {index + 1}. {element}
                            </a>
                          </li>
                        )
                      })
                    }
            </ul>
            </div>

          : ''
      }
        </main>

      </div>
    </div>
  )
}

export default App
