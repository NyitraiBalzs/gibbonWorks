import React from 'react'


const Results = ({title, link, description}) => {
  return (  
    <div id='results'>
        <h1 className='result-titles'><a href={link}>{title}</a></h1>
        <ul>
            <li className='result-description'>{description}</li>
        </ul>
    </div>
  )
}

export default Results