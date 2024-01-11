import './App.css';
import Navbar from './components/Navbar/Navbar';
import FileUpload from './components/FileUpload/FileUpload';
import Footer from './components/Footer/Footer';
import SongsList from './components/SongsList/SongsList';
import { useState } from 'react';
import LoadingScreen from './components/LoadingScreen/LoadingScreen';

function App() {
  const [songsData, setSongsData] = useState(null)
  const [loadingScreen, setLoadingScreen] = useState(false)

  const handleSongsData = (data) => {
    setSongsData(data);
  }

  const handleLoadingScreen = (data) => {
    setLoadingScreen(data);
  }

  return (
    <div className='app-content-holder'>
      <Navbar></Navbar>
      {songsData === null && loadingScreen === false && (
        <FileUpload handleSongsData={handleSongsData} handleLoadingScreen={handleLoadingScreen}></FileUpload>
      )}
      { songsData !== null && loadingScreen === false && (
        <SongsList songsData={songsData}></SongsList>
      ) }
      {loadingScreen && (
        <LoadingScreen></LoadingScreen>
      )}
      <Footer></Footer>
    </div>
  );
}

export default App;
