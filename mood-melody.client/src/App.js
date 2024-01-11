import './App.css';
import Navbar from './components/Navbar/Navbar';
import FileUpload from './components/FileUpload/FileUpload';
import Footer from './components/Footer/Footer';
import SongsList from './components/SongsList/SongsList';
import { useState } from 'react';

function App() {
  const [songsData, setSongsData] = useState(null)

  const handleSongsData = (data) => {
    setSongsData(data);
  }

  return (
    <div className='app-content-holder'>
      <Navbar></Navbar>
      {songsData === null ? (
        <FileUpload handleSongsData={handleSongsData}></FileUpload>
      ) :(
        <SongsList songsData={songsData}></SongsList>
      ) }
      <Footer></Footer>
    </div>
  );
}

export default App;
