import React from 'react'

const Results = ({title, link, description}) => {
  return (  
    <div id='results'>
        <h2 className='result-titles'><a href={link}>{title}</a></h2>
        
        <ul>
            <li className='result-description'>{description}</li>
        </ul>
    </div>
  )
}

export default Results