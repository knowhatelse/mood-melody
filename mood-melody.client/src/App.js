import './App.css';
import Navbar from './components/Navbar/Navbar';
import FileUpload from './components/FileUpload/FileUpload';
import Footer from './components/Footer/Footer';
import SongsList from './components/SongsList/SongsList';

function App() {
  return (
    <div className='app-content-holder'>
      <Navbar></Navbar>
      <FileUpload></FileUpload>
      {/*<SongsList></SongsList> */}
      <Footer></Footer>
    </div>
  );
}

export default App;
