import React from 'react';
import Header from './componetnts/Header';
import Footer from './componetnts/Footer';
import ChatWindow from './componetnts/ChatWindow';

function App() {
  const user = 'Anutád'
  return (
      <div className='container'>
        <Header user={user}/>
        <ChatWindow/>
        <Footer user={user}/>
    </div>
  );
}

export default App;
