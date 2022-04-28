import React from 'react'
import { useState } from 'react'
import Results from './Results'

const Window = () => {
  const [text, setText] = useState('')
  const [data, setData] = useState({})
  const handleInput = async () => {
    const options = {
      method: 'GET',
      headers: {
        'X-User-Agent': 'desktop',
        'X-Proxy-Location': 'EU',
        'X-RapidAPI-Host': 'google-search3.p.rapidapi.com',
        'X-RapidAPI-Key': '89f6583f5fmsh60c56cb9dc212f7p17fb11jsn50d1408b82f3'
      }
    };
    let url = `https://google-search3.p.rapidapi.com/api/v1/search/q=${text.replace(' ', '+')}`
    const response = await fetch(url, options)
    const json = await response.json()
    setData(json)
    console.log(data)

  }

  return (
    <div id='window'>
      <div id='input-field-container'>
        <input type="text" id='input-field' onChange={(e) => setText(e.target.value)} />
        <button id='input-btn' onClick={handleInput}>Search</button>
      </div>
      <div>
        {data.results ?
          data.results.map(item => (<Results title={item.title} link={item.link} description={item.description} />)) :
          <></>}
      </div>
    </div>
  )
}

export default Window