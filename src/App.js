import React from 'react';
import Header from './componetnts/Header';
import Footer from './componetnts/Footer';
import Window from './componetnts/Window';

function App() {
  const user = 'Nyitrai Én'
  const pageTitle = 'Bootleg Google'

  return (
      <div id='container'>
        <Header pageTitle={pageTitle}/>
        <Window/>
        <Footer user={user}/>
    </div>
  );
}

export default App;
