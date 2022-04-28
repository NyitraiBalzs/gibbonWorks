import React from 'react'

const Results = ({title, link, description}) => {
  return (  
    <div id='results'>
        <h3 className='result-titles'><a href={link}>{title}</a></h3>
        <button>dolgok</button>
        
        <ul>
            <li className='result-description'>{description}</li>
        </ul>
    </div>
  )
}

export default Results